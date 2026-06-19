// DDS v2.0 Tailwind preset (생성 파일 — 직접 수정 금지)
// regenerate: python3 scripts/build_tokens.py
// 사용: presets: [require('./dist/tokens.tailwind.js')] + dist/tokens.css import
module.exports = {
  "theme": {
    "extend": {
      "colors": {
        "text": {
          "primary": "var(--color-text-primary)",
          "secondary": "var(--color-text-secondary)",
          "tertiary": "var(--color-text-tertiary)",
          "warning": "var(--color-text-warning)",
          "success": "var(--color-text-success)",
          "info": "var(--color-text-info)",
          "danger": "var(--color-text-danger)",
          "info-bold": "var(--color-text-info-bold)",
          "warning-bold": "var(--color-text-warning-bold)",
          "success-bold": "var(--color-text-success-bold)",
          "danger-bold": "var(--color-text-danger-bold)",
          "interactive-primary": "var(--color-text-interactive-primary)",
          "interactive-primary-hover": "var(--color-text-interactive-primary-hover)",
          "interactive-primary-pressed": "var(--color-text-interactive-primary-pressed)",
          "interactive-secondary": "var(--color-text-interactive-secondary)",
          "interactive-secondary-hover": "var(--color-text-interactive-secondary-hover)",
          "interactive-disabled": "var(--color-text-interactive-disabled)",
          "interactive-selected": "var(--color-text-interactive-selected)",
          "interactive-visited": "var(--color-text-interactive-visited)",
          "interactive-inverse": "var(--color-text-interactive-inverse)",
          "disabled": "var(--color-text-disabled)"
        },
        "icon": {
          "primary": "var(--color-icon-primary)",
          "secondary": "var(--color-icon-secondary)",
          "tertiary": "var(--color-icon-tertiary)",
          "info": "var(--color-icon-info)",
          "warning": "var(--color-icon-warning)",
          "success": "var(--color-icon-success)",
          "danger": "var(--color-icon-danger)",
          "disabled": "var(--color-icon-disabled)",
          "interactive-primary": "var(--color-icon-interactive-primary)",
          "interactive-primary-hover": "var(--color-icon-interactive-primary-hover)",
          "interactive-primary-pressed": "var(--color-icon-interactive-primary-pressed)",
          "interactive-secondary": "var(--color-icon-interactive-secondary)",
          "interactive-secondary-hover": "var(--color-icon-interactive-secondary-hover)",
          "interactive-secondary-pressed": "var(--color-icon-interactive-secondary-pressed)",
          "interactive-selected": "var(--color-icon-interactive-selected)",
          "interactive-visited": "var(--color-icon-interactive-visited)",
          "interactive-inverse": "var(--color-icon-interactive-inverse)"
        },
        "bg": {
          "primary": "var(--color-bg-primary)",
          "secondary": "var(--color-bg-secondary)",
          "tertiary": "var(--color-bg-tertiary)",
          "info": "var(--color-bg-info)",
          "warning": "var(--color-bg-warning)",
          "success": "var(--color-bg-success)",
          "danger": "var(--color-bg-danger)",
          "info-bold": "var(--color-bg-info-bold)",
          "warning-bold": "var(--color-bg-warning-bold)",
          "success-bold": "var(--color-bg-success-bold)",
          "danger-bold": "var(--color-bg-danger-bold)",
          "disabled": "var(--color-bg-disabled)",
          "interactive-primary": "var(--color-bg-interactive-primary)",
          "interactive-primary-hover": "var(--color-bg-interactive-primary-hover)",
          "interactive-primary-pressed": "var(--color-bg-interactive-primary-pressed)",
          "interactive-secondary": "var(--color-bg-interactive-secondary)",
          "interactive-secondary-hover": "var(--color-bg-interactive-secondary-hover)",
          "interactive-secondary-pressed": "var(--color-bg-interactive-secondary-pressed)",
          "interactive-selected": "var(--color-bg-interactive-selected)",
          "inverse-bold": "var(--color-bg-inverse-bold)",
          "primary-subtle": "var(--color-bg-primary-subtle)",
          "success-subtle": "var(--color-bg-success-subtle)",
          "info-subtle": "var(--color-bg-info-subtle)",
          "warning-subtle": "var(--color-bg-warning-subtle)",
          "danger-subtle": "var(--color-bg-danger-subtle)"
        },
        "border": {
          "primary": "var(--color-border-primary)",
          "secondary": "var(--color-border-secondary)",
          "focusing": "var(--color-border-focusing)",
          "info": "var(--color-border-info)",
          "warning": "var(--color-border-warning)",
          "success": "var(--color-border-success)",
          "danger": "var(--color-border-danger)",
          "info-bold": "var(--color-border-info-bold)",
          "warning-bold": "var(--color-border-warning-bold)",
          "success-bold": "var(--color-border-success-bold)",
          "disabled": "var(--color-border-disabled)",
          "interactive-primary": "var(--color-border-interactive-primary)",
          "interactive-primary-hover": "var(--color-border-interactive-primary-hover)",
          "interactive-primary-pressed": "var(--color-border-interactive-primary-pressed)",
          "interactive-secondary": "var(--color-border-interactive-secondary)",
          "interactive-secondary-hover": "var(--color-border-interactive-secondary-hover)",
          "interactive-secondary-pressed": "var(--color-border-interactive-secondary-pressed)",
          "interactive-selected": "var(--color-border-interactive-selected)"
        },
        "accent": {
          "violet-subtle": "var(--color-accent-violet-subtle)",
          "violet": "var(--color-accent-violet)",
          "violet-bold": "var(--color-accent-violet-bold)",
          "pink-subtle": "var(--color-accent-pink-subtle)",
          "pink": "var(--color-accent-pink)",
          "pink-bold": "var(--color-accent-pink-bold)",
          "orange-subtle": "var(--color-accent-orange-subtle)",
          "orange": "var(--color-accent-orange)",
          "orange-bold": "var(--color-accent-orange-bold)",
          "cyan-subtle": "var(--color-accent-cyan-subtle)",
          "cyan": "var(--color-accent-cyan)",
          "cyan-bold": "var(--color-accent-cyan-bold)",
          "mint-subtle": "var(--color-accent-mint-subtle)",
          "mint": "var(--color-accent-mint)",
          "mint-bold": "var(--color-accent-mint-bold)",
          "amber-subtle": "var(--color-accent-amber-subtle)",
          "amber": "var(--color-accent-amber)",
          "amber-bold": "var(--color-accent-amber-bold)"
        },
        "chart": {
          "1": "var(--color-chart-1)",
          "2": "var(--color-chart-2)",
          "3": "var(--color-chart-3)",
          "4": "var(--color-chart-4)",
          "5": "var(--color-chart-5)",
          "6": "var(--color-chart-6)",
          "7": "var(--color-chart-7)",
          "8": "var(--color-chart-8)"
        }
      },
      "spacing": {
        "0": "var(--space-0)",
        "2": "var(--space-2)",
        "4": "var(--space-4)",
        "8": "var(--space-8)",
        "12": "var(--space-12)",
        "16": "var(--space-16)",
        "24": "var(--space-24)",
        "32": "var(--space-32)",
        "40": "var(--space-40)",
        "48": "var(--space-48)",
        "64": "var(--space-64)"
      },
      "borderRadius": {
        "sm": "var(--radius-sm)",
        "md": "var(--radius-md)",
        "lg": "var(--radius-lg)",
        "xl": "var(--radius-xl)",
        "2xl": "var(--radius-2xl)",
        "rounded": "var(--radius-rounded)"
      },
      "boxShadow": {
        "sm": "var(--shadow-sm)",
        "md": "var(--shadow-md)",
        "lg": "var(--shadow-lg)",
        "xl": "var(--shadow-xl)"
      },
      "transitionTimingFunction": {
        "standard": "var(--motion-easing-standard)",
        "decelerate": "var(--motion-easing-decelerate)",
        "accelerate": "var(--motion-easing-accelerate)",
        "emphasized": "var(--motion-easing-emphasized)",
        "spring-soft": "var(--motion-easing-spring-soft)",
        "spring-snappy": "var(--motion-easing-spring-snappy)"
      },
      "transitionDuration": {
        "instant": "var(--motion-duration-instant)",
        "quick": "var(--motion-duration-quick)",
        "base": "var(--motion-duration-base)",
        "moderate": "var(--motion-duration-moderate)",
        "slow": "var(--motion-duration-slow)",
        "deliberate": "var(--motion-duration-deliberate)"
      }
    }
  }
};
