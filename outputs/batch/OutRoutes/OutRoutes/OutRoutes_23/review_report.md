# Play-Annotation-Generator Annotation Review — OutRoutes_23

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_23`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 59
- **Validation Warnings:** 59
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 37
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `7` | `7` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `14` | `14` | 32 | START | 32 | 36 |
| ✅ EXACT | `Action_PassBlock` | RG | `18` | `18` | 32 | START | 32 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 32 | START | 32 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `20` | `20` | 32 | START | 32 | 52 |
| ✅ EXACT | `Action_PassBlock` | LT | `9` | `9` | 32 | START | 32 | 150 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `7` | `7` | 38 | START | 38 | 109 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 38 | END | 38 | 38 |
| ✅ EXACT | `Action_ThrowPass` | QB | `15` | `15` | 77 | START | 77 | 85 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `7` | `7` | 110 | START | 110 | 127 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `7` | `7` | 128 | START | 128 | 149 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_SnapReceive` | 38 | 38 | 1 | inferred_complete_timeline |
| `Action_None` | 39 | 76 | 38 | inferred_complete_timeline |
| `Action_ThrowPass` | 77 | 85 | 9 | inferred_complete_timeline |
| `Action_None` | 86 | 150 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 150 | 98 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_RunOutRoute` | 38 | 109 | 72 | inferred_complete_timeline |
| `Action_SecureCatch` | 110 | 127 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 128 | 149 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 150 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 52 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 73 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 90 | 150 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 36 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 139 | 53 | inferred_complete_timeline |
| `Action_PassBlock` | 142 | 150 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 150 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 52 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 150 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 68 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 82 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 88 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 62 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 71 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 81 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
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
| `22` | `23` | Position_Unknown | Team_Unknown | 87–150 | 61 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 92–150 | 52 | 5 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 105–150 | 25 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 109–113 | 5 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 113–150 | 38 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 47 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-140] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [128-149] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-36] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [87-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [142-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-68] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-82] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-88] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-150] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-52] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-60] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-73] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [90-150] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-52] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [60-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-62] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-71] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-91] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-150] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-98] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-104] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-133] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-110] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-121] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-150] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-113] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-150] for track '26' has 1 frames without a visible bounding box.
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