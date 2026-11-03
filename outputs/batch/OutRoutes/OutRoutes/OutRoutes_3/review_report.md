# Play-Annotation-Generator Annotation Review — OutRoutes_3

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_3`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 66
- **Validation Warnings:** 93
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 46
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `21` | `Group` |
| ✅ EXACT | `Action_RunOutRoute` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `14` | `14` |
| ✅ EXACT | `Action_SecureCatch` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `21` | `Group` | 0 | START | 0 | 32 |
| ✅ EXACT | `Action_RunOutRoute` | WR1 | `0` | `0` | 14 | START | 14 | 84 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 14 | END | 14 | 14 |
| ✅ EXACT | `Action_ThrowPass` | RB | `14` | `14` | 46 | START | 46 | 54 |
| ✅ EXACT | `Action_SecureCatch` | WR1 | `0` | `0` | 85 | START | 85 | 88 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `0` | `0` | 89 | START | 89 | 150 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_SnapReceive` | 14 | 14 | 1 | inferred_complete_timeline |
| `Action_None` | 15 | 150 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_ThrowPass` | 46 | 54 | 9 | inferred_complete_timeline |
| `Action_None` | 55 | 113 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_RunOutRoute` | 14 | 84 | 71 | inferred_complete_timeline |
| `Action_SecureCatch` | 85 | 88 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 89 | 150 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 39 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 101 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 111 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–17
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–40
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 25 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 35 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 40 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 113 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–34
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 150 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–87 | 88 | 1 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–101 | 102 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–137 | 112 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 28–115 | 43 | 14 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 33–34 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 41–115 | 71 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 43–48 | 6 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 53–150 | 98 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 71–110 | 40 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 72–107 | 36 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 84–85 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 86–90 | 5 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 96–101 | 6 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 121–139 | 19 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 135–138 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 5, Column 'Pass Block': Could not parse frame number from '-' in entry '-,OL'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 7: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ Row 8: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_BallCarry' range [89-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-90] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-113] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-101] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-100] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-150] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-111] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-111] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-25] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-35] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-40] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-39] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-101] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-109] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-137] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-32] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-38] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-48] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-52] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-60] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-65] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-70] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-77] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-91] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-97] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-107] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-115] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-34] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-49] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-107] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-115] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-48] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-110] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-107] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-90] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-101] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-139] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-138] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.

</details>