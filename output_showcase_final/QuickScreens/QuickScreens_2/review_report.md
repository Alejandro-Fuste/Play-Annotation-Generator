# Play-Annotation-Generator Annotation Review — QuickScreens_2

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `QuickScreens_2`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_QuickScreens`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 54
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 4
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowScreenPass` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `20` | `16` |
| ✅ EXACT | `Action_RunAfterCatch` | Position_Unknown | Team_Unknown | `20` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `3` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 7 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `9` | `9` | 21 | START | 21 | 35 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `6` | 35 | END | 21 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowScreenPass` | QB | `6` | `6` | 48 | START | 48 | 50 |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | `20` | `16` | 85 | START | 85 | 93 |
| ✅ EXACT | `Action_RunAfterCatch` | Position_Unknown | `20` | `16` | 101 | START | 101 | 105 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_SnapReceive` | 21 | 35 | 15 | inferred_complete_timeline |
| `Action_None` | 36 | 47 | 12 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 48 | 50 | 3 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 52 | 57 | 6 | inferred_complete_timeline |
| `Action_None` | 58 | 68 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 66 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 33 | 72 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–7
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 64 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 71 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–63
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 63 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 68 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 59 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 15–69 | 55 | 3 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 64–210 | 147 | 1 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 73–204 | 120 | 3 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 74–210 | 130 | 5 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 76–210 | 126 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 77–95 | 12 | 2 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 81–131 | 39 | 2 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 85–105 | 21 | 3 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 99–197 | 91 | 3 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 107–144 | 38 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 138–157 | 20 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 145–148 | 4 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 147–210 | 63 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 151–210 | 60 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 155–210 | 56 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 165–175 | 11 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 192–210 | 19 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ThrowScreenPass` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 40 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [21-59] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-63] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-71] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-64] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-72] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-66] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowScreenPass' range [48-50] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-68] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-68] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-69] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-167] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-204] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-170] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-185] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-199] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-157] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-116] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [101-105] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-114] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-162] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-197] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-144] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-157] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-182] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-175] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>