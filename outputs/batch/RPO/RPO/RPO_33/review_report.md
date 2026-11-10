# Play-Annotation-Generator Annotation Review — RPO_33

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_33`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 1
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `9` | `9` |
| ⚠️ START CHANGED | `Action_ReadDefender` | QB | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBall` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 3 | START | 3 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 3 | START | 3 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 3 | START | 3 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 3 | START | 3 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 3 | START | 3 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 3 | START | 3 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 3 | START | 3 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `11` | `11` | 50 | START | 50 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `3` | `3` | 50 | START | 50 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `6` | `6` | 50 | START | 50 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `7` | `7` | 50 | START | 50 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `9` | `9` | 50 | START | 50 | 57 |
| ⚠️ START CHANGED | `Action_ReadDefender` | QB | `4` | `4` | 54 | START | 55 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBall` | QB | `4` | `4` | 77 | START | 77 | 82 |
| ✅ EXACT | `Action_ThrowPass` | QB | `4` | `4` | 134 | START | 134 | 141 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 3–159
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 48 | 46 | inferred_complete_timeline |
| `Action_None` | 49 | 52 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 55 | 76 | 22 | inferred_complete_timeline |
| `Action_PullBall` | 77 | 82 | 6 | inferred_complete_timeline |
| `Action_PullBall` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_None` | 106 | 133 | 28 | inferred_complete_timeline |
| `Action_ThrowPass` | 134 | 141 | 8 | inferred_complete_timeline |
| `Action_None` | 142 | 159 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 3–109
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 48 | 46 | inferred_complete_timeline |
| `Action_None` | 49 | 54 | 6 | inferred_complete_timeline |
| `Action_None` | 56 | 82 | 27 | inferred_complete_timeline |
| `Action_None` | 107 | 109 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 3–191
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 48 | 46 | inferred_complete_timeline |
| `Action_None` | 49 | 49 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 133 | 84 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 140 | 5 | inferred_complete_timeline |
| `Action_None` | 144 | 154 | 11 | inferred_complete_timeline |
| `Action_None` | 159 | 191 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 3–158
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 48 | 46 | inferred_complete_timeline |
| `Action_None` | 49 | 49 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 52 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 141 | 78 | inferred_complete_timeline |
| `Action_None` | 142 | 158 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 3–160
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 48 | 46 | inferred_complete_timeline |
| `Action_None` | 49 | 49 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 57 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 135 | 11 | inferred_complete_timeline |
| `Action_None` | 142 | 145 | 4 | inferred_complete_timeline |
| `Action_None` | 147 | 160 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 3–135
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 48 | 46 | inferred_complete_timeline |
| `Action_None` | 49 | 49 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 89 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 102 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 135 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 3–134
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 48 | 46 | inferred_complete_timeline |
| `Action_None` | 49 | 49 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 115 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 134 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 3–186
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 48 | 46 | inferred_complete_timeline |
| `Action_None` | 49 | 146 | 98 | inferred_complete_timeline |
| `Action_None` | 165 | 186 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 3–154
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 48 | 46 | inferred_complete_timeline |
| `Action_None` | 49 | 84 | 36 | inferred_complete_timeline |
| `Action_None` | 90 | 109 | 20 | inferred_complete_timeline |
| `Action_None` | 111 | 118 | 8 | inferred_complete_timeline |
| `Action_None` | 128 | 136 | 9 | inferred_complete_timeline |
| `Action_None` | 138 | 154 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 3–133
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 7 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 21 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 48 | 2 | inferred_complete_timeline |
| `Action_None` | 49 | 113 | 65 | inferred_complete_timeline |
| `Action_None` | 116 | 133 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 3–148
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 48 | 46 | inferred_complete_timeline |
| `Action_None` | 49 | 148 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 3–144
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 48 | 46 | inferred_complete_timeline |
| `Action_None` | 49 | 111 | 63 | inferred_complete_timeline |
| `Action_None` | 113 | 129 | 17 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 3–127
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 48 | 46 | inferred_complete_timeline |
| `Action_None` | 49 | 115 | 67 | inferred_complete_timeline |
| `Action_None` | 118 | 127 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 46–59 | 13 | 3 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 60–67 | 8 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 80–186 | 102 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 96–125 | 30 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 120–329 | 210 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 139–148 | 10 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 142–153 | 6 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 144–167 | 24 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 153–187 | 35 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 154–329 | 176 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 157–161 | 5 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 159–219 | 60 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 161–207 | 47 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 241–242 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ `Action_ReadDefender` for actor_track_id `4` (QB): Annotated start 54 != Inferred start 55
- ⚠️ Ambiguous match for action `Action_PullBall` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (LT) duration 92 frames exceeds threshold 90 frames [start=50, end=141].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (LG) duration 92 frames exceeds threshold 90 frames [start=50, end=141].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (C) duration 92 frames exceeds threshold 90 frames [start=50, end=141].
- ⚠️ Action 'Action_None' range [49-115] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-127] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-146] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-186] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-84] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-109] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-118] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-136] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-154] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-133] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [136-140] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-154] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-191] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-52] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBall' range [77-82] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBall' range [95-97] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-133] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-159] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-111] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-129] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-89] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [100-102] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-52] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-158] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-54] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-82] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-57] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [125-135] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-160] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-148] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-48] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-115] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [132-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-7] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-21] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-113] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-133] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-53] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-59] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-67] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-178] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-125] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-329] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-148] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-167] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-187] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-210] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-219] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-207] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.

</details>