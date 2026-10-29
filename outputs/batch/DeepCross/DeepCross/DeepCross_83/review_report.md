# Play-Annotation-Generator Annotation Review — DeepCross_83

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_83`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Completion`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 132
- **Validation Warnings:** 149
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 116
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB1 | defense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | Position_Unknown | Team_Unknown | `22` | `22` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `10` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 28 |
| ✅ EXACT | `Action_BallSnap` | CB1 | `13` | `13` | 24 | START | 24 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `12` | `12` | 29 | START | 29 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `15` | `15` | 29 | START | 29 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `18` | `18` | 29 | START | 29 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `21` | `21` | 29 | START | 29 | 43 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 30 | END | 24 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | Position_Unknown | `22` | `22` | 40 | START | 60 | 139 |
| ✅ EXACT | `Action_ThrowPass` | QB | `19` | `19` | 123 | START | 123 | 130 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_SnapReceive` | 24 | 30 | 7 | inferred_complete_timeline |
| `Action_None` | 31 | 45 | 15 | inferred_complete_timeline |
| `Action_None` | 47 | 122 | 76 | inferred_complete_timeline |
| `Action_ThrowPass` | 123 | 130 | 8 | inferred_complete_timeline |
| `Action_None` | 131 | 131 | 1 | inferred_complete_timeline |
| `Action_None` | 133 | 137 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 67 | 44 | inferred_complete_timeline |
| `Action_None` | 71 | 113 | 43 | inferred_complete_timeline |
| `Action_None` | 115 | 173 | 59 | inferred_complete_timeline |
| `Action_None` | 175 | 185 | 11 | inferred_complete_timeline |
| `Action_None` | 192 | 194 | 3 | inferred_complete_timeline |
| `Action_None` | 202 | 205 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 239 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 66 | 43 | inferred_complete_timeline |
| `Action_None` | 68 | 80 | 13 | inferred_complete_timeline |
| `Action_None` | 89 | 91 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 43 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 57 | 68 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 150 | 163 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 172 | 192 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 194 | 206 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 216 | 232 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 43 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 118 | 145 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 43 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 65 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–54
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 43 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 54 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 44 | 21 | inferred_complete_timeline |
| `Action_None` | 46 | 49 | 4 | inferred_complete_timeline |
| `Action_None` | 51 | 65 | 15 | inferred_complete_timeline |
| `Action_None` | 79 | 80 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 46 | 23 | inferred_complete_timeline |
| `Action_None` | 52 | 65 | 14 | inferred_complete_timeline |
| `Action_None` | 68 | 78 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 43 | 20 | inferred_complete_timeline |
| `Action_None` | 52 | 65 | 14 | inferred_complete_timeline |
| `Action_None` | 101 | 132 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 43 | 20 | inferred_complete_timeline |
| `Action_None` | 52 | 65 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–55
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_BallSnap` | 24 | 30 | 7 | inferred_complete_timeline |
| `Action_None` | 31 | 42 | 12 | inferred_complete_timeline |
| `Action_None` | 53 | 55 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 201 | 178 | inferred_complete_timeline |
| `Action_None` | 206 | 210 | 5 | inferred_complete_timeline |
| `Action_None` | 215 | 216 | 2 | inferred_complete_timeline |
| `Action_None` | 219 | 223 | 5 | inferred_complete_timeline |
| `Action_None` | 227 | 239 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 103 | 80 | inferred_complete_timeline |
| `Action_None` | 108 | 239 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 239 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 70 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 53 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–108 | 109 | 2 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–239 | 194 | 15 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–163 | 161 | 5 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 60–205 | 139 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 103–239 | 137 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 106–231 | 119 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 122–239 | 118 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 138–200 | 23 | 3 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 138–140 | 3 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 171–239 | 53 | 7 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 172–226 | 51 | 4 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 173–223 | 48 | 3 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 180–189 | 9 | 2 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 184–203 | 15 | 3 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 184–197 | 8 | 2 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 188–192 | 5 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 220–228 | 9 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 223–228 | 6 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 234–237 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (6 segments found)
- ⚠️ Ambiguous match for action `Action_RunDeepCrossRoute` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF3` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 103 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 86: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 86: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 86: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 86: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ Row 86: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [24-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-108] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-67] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-113] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-173] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-185] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-70] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-53] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-103] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-239] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-83] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-89] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-105] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-145] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-179] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-192] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-213] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-147] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-155] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-66] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-80] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-201] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-223] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-43] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-54] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-42] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-55] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-46] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-65] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-78] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-43] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [110-111] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [118-145] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-44] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-49] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-65] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-43] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-65] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-43] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-65] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-45] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 131, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [131-131] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-137] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-43] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-65] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-132] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-43] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [57-68] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [150-163] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [172-192] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [194-206] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [216-232] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [60-139] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [147-200] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-205] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-207] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-231] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-189] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-200] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-187] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-207] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-195] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-207] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-226] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-179] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-189] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-223] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-203] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-189] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-192] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-228] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-228] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.

</details>