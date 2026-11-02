# Play-Annotation-Generator Annotation Review — JetSweep_236

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_236`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 106
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `3` | `2` |
| ✅ EXACT | `Action_BallSnap` | DT1 | defense | `19` | `18` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `6` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_Toss` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_BallCarry` | WR | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `3` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 87 |
| ✅ EXACT | `Action_JetMotion` | WR | `3` | `2` | 52 | START | 52 | 109 |
| ✅ EXACT | `Action_BallSnap` | DT1 | `19` | `18` | 87 | START | 87 | 96 |
| ✅ EXACT | `Action_LeadBlock` | TE | `8` | `7` | 88 | START | 88 | 124 |
| ✅ EXACT | `Action_ZoneBlock` | C | `17` | `16` | 88 | START | 88 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `4` | `3` | 88 | START | 88 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `5` | `4` | 88 | START | 88 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `6` | `5` | 88 | START | 88 | 104 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `6` | 88 | START | 88 | 134 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 96 | END | 87 | 96 |
| ✅ EXACT | `Action_Toss` | QB | `18` | `17` | 106 | START | 106 | 109 |
| ✅ EXACT | `Action_BallCarry` | WR | `3` | `2` | 110 | START | 110 | 139 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 134 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_SnapReceive` | 87 | 96 | 10 | inferred_complete_timeline |
| `Action_None` | 97 | 105 | 9 | inferred_complete_timeline |
| `Action_Toss` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_None` | 110 | 269 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_JetMotion` | 52 | 109 | 58 | inferred_complete_timeline |
| `Action_BallCarry` | 110 | 139 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_LeadBlock` | 88 | 124 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 134 | 47 | inferred_complete_timeline |
| `Action_None` | 135 | 151 | 17 | inferred_complete_timeline |
| `Action_None` | 163 | 269 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 134 | 47 | inferred_complete_timeline |
| `Action_None` | 135 | 257 | 123 | inferred_complete_timeline |
| `Action_None` | 259 | 266 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 134 | 47 | inferred_complete_timeline |
| `Action_None` | 135 | 269 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 104 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 134 | 29 | inferred_complete_timeline |
| `Action_None` | 135 | 170 | 36 | inferred_complete_timeline |
| `Action_None` | 181 | 249 | 69 | inferred_complete_timeline |
| `Action_None` | 259 | 260 | 2 | inferred_complete_timeline |
| `Action_None` | 264 | 266 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 130 | 43 | inferred_complete_timeline |
| `Action_None` | 143 | 146 | 4 | inferred_complete_timeline |
| `Action_None` | 148 | 155 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 86 | 12 | inferred_complete_timeline |
| `Action_None` | 87 | 269 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 269 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 14 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 18 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 86 | 8 | inferred_complete_timeline |
| `Action_BallSnap` | 87 | 96 | 10 | inferred_complete_timeline |
| `Action_None` | 97 | 269 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 92 | 6 | inferred_complete_timeline |
| `Action_None` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_None` | 104 | 106 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–181
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 168 | 82 | inferred_complete_timeline |
| `Action_None` | 170 | 181 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 115 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 198 | 112 | inferred_complete_timeline |
| `Action_None` | 201 | 204 | 4 | inferred_complete_timeline |
| `Action_None` | 220 | 256 | 37 | inferred_complete_timeline |
| `Action_None` | 258 | 269 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–6
- **Visible Samples:** 7

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 86 | 49 | inferred_complete_timeline |
| `Action_None` | 87 | 174 | 88 | inferred_complete_timeline |
| `Action_None` | 181 | 196 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 175 | 89 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–179 | 176 | 4 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 100–142 | 43 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 115–269 | 154 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 119–166 | 16 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 122–268 | 139 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 152–269 | 92 | 5 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 156–240 | 76 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 157–269 | 110 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 157–194 | 20 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 159–269 | 108 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 161–181 | 21 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 176–269 | 84 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 178–236 | 58 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 182–250 | 68 | 2 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 187–269 | 77 | 3 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 203–269 | 62 | 4 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 217–269 | 53 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 247–250 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 474: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [87-158] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-173] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-115] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [110-139] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-130] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-155] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-257] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-266] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-104] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-170] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-249] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-151] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [88-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-198] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-256] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-92] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-196] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-168] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-181] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-83] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-134] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-14] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-18] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-142] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-209] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-126] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-243] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-268] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-162] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-189] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-206] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-240] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-215] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-174] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-206] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-226] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-181] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-241] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-211] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-236] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-213] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-250] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-206] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-234] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-269] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>