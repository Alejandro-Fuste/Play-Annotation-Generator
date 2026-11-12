# Play-Annotation-Generator Annotation Review — SplitZone_57

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_57`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 97
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `23` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `26` | `22` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `14` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `23` | `Group` | 0 | START | 73 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `4` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 85 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 86 | START | 86 | 102 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `16` | `16` | 89 | START | 89 | 150 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `17` | `17` | 89 | START | 89 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `20` | 89 | START | 103 | 116 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `23` | `21` | 89 | START | 89 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `3` | `3` | 89 | START | 89 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | `4` | `4` | 94 | START | 94 | 124 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `19` | `19` | 102 | END | 86 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | `26` | `22` | 103 | START | 106 | 129 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `19` | `19` | 109 | START | 109 | 116 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `14` | `14` | 117 | START | 117 | 200 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 150 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 117 | 200 | 84 | inferred_complete_timeline |
| `Action_BallCarry` | 234 | 235 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_SplitBlock` | 94 | 124 | 31 | inferred_complete_timeline |
| `Action_SplitBlock` | 135 | 150 | 16 | inferred_complete_timeline |
| `Action_None` | 151 | 190 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 299 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 299 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–294
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 294 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 112 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 116 | 118 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 150 | 62 | inferred_complete_timeline |
| `Action_None` | 151 | 299 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_BallSnap` | 86 | 102 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 116 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 119 | 150 | 32 | inferred_complete_timeline |
| `Action_None` | 151 | 299 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `23`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 73–107
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 86 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 88 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 107 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 150 | 62 | inferred_complete_timeline |
| `Action_None` | 151 | 299 | 149 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 150 | 65 | inferred_complete_timeline |
| `Action_None` | 205 | 244 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 231 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 160 | 75 | inferred_complete_timeline |
| `Action_None` | 166 | 172 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 299 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 131 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 151 | 66 | inferred_complete_timeline |
| `Action_None` | 160 | 299 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 299 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–284
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 246 | 161 | inferred_complete_timeline |
| `Action_None` | 250 | 284 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–277
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 139 | 54 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 148 | 151 | 4 | inferred_complete_timeline |
| `Action_None` | 153 | 192 | 40 | inferred_complete_timeline |
| `Action_None` | 195 | 277 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 180 | 95 | inferred_complete_timeline |
| `Action_None` | 184 | 226 | 43 | inferred_complete_timeline |
| `Action_None` | 228 | 231 | 4 | inferred_complete_timeline |
| `Action_None` | 235 | 299 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 220 | 135 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–220 | 221 | 5 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 106–299 | 185 | 5 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 129–150 | 22 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 141–299 | 159 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 142–299 | 153 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 142–144 | 3 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 159–187 | 29 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 164–299 | 134 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 185–299 | 114 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 197–299 | 103 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 199–226 | 8 | 3 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 241–299 | 59 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 242–299 | 54 | 3 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 251–286 | 36 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 262–277 | 13 | 2 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 275–276 | 2 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 278–299 | 12 | 3 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 297–299 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `22` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 116: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [86–102], lower_priority='Action_ZoneBlock' annotated_start=89, effective_Action_ZoneBlock_start=103.
- ⚠️ Action 'Action_None' range [86-294] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-231] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-112] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [116-118] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [94-124] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [135-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-190] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-244] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-131] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-160] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-172] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-220] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-151] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-226] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-231] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-246] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-284] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-139] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-151] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-192] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-277] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [117-200] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [234-235] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-220] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-116] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-86] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-107] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [106-129] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [131-139] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [142-143] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-187] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-299] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-262] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-270] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-299] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-286] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-277] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-282] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-296] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.

</details>