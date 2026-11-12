# Play-Annotation-Generator Annotation Review — SplitZone_267

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_267`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 65
- **Validation Warnings:** 58
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 45
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `3` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `5` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 28 | START | 28 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 28 | START | 28 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `15` | `Group` | 28 | START | 28 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 28 | START | 28 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 28 | START | 28 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 28 | START | 28 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 28 | START | 28 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 28 | START | 28 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 28 | START | 28 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 28 | START | 28 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 28 | START | 28 | 122 |
| ✅ EXACT | `Action_SplitBlock` | TE | `4` | `4` | 123 | START | 123 | 201 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `16` | 123 | START | 123 | 137 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `18` | `18` | 123 | START | 123 | 211 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `21` | 123 | START | 123 | 158 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `8` | 123 | START | 123 | 211 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `9` | 123 | START | 123 | 168 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `3` | 129 | END | 129 | 129 |
| ✅ EXACT | `Action_Handoff` | QB | `3` | `3` | 136 | START | 136 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `5` | `5` | 153 | START | 153 | 271 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 211 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 28–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 128 | 101 | inferred_complete_timeline |
| `Action_SnapReceive` | 129 | 129 | 1 | inferred_complete_timeline |
| `Action_None` | 130 | 135 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 136 | 152 | 17 | inferred_complete_timeline |
| `Action_None` | 153 | 299 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 28–299
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 152 | 125 | inferred_complete_timeline |
| `Action_BallCarry` | 153 | 271 | 119 | inferred_complete_timeline |
| `Action_BallCarry` | 275 | 297 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 299 | 299 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 28–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 299 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 28–133
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 133 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 28–109
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 109 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 28–299
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 122 | 95 | inferred_complete_timeline |
| `Action_SplitBlock` | 123 | 201 | 79 | inferred_complete_timeline |
| `Action_None` | 214 | 217 | 4 | inferred_complete_timeline |
| `Action_None` | 241 | 250 | 10 | inferred_complete_timeline |
| `Action_None` | 253 | 273 | 21 | inferred_complete_timeline |
| `Action_None` | 280 | 299 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 28–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 122 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 211 | 89 | inferred_complete_timeline |
| `Action_None` | 212 | 299 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 28–158
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 122 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 158 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 28–299
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 122 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 137 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 165 | 211 | 47 | inferred_complete_timeline |
| `Action_None` | 212 | 299 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 28–299
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 122 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 168 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 179 | 186 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 191 | 211 | 21 | inferred_complete_timeline |
| `Action_None` | 212 | 299 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 28–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 122 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 211 | 89 | inferred_complete_timeline |
| `Action_None` | 212 | 299 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 28–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 299 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 28–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 299 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 28–180
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 180 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 28–154
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 154 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 28–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 299 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 28–265
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 265 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 28–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 299 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 28–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 299 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 28–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 299 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 28–299
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 281 | 254 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 288 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 299 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 28–292
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 281 | 254 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 292 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 108–299 | 192 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 132–299 | 165 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 167–299 | 133 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 179–299 | 121 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 198–299 | 102 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 226–227 | 2 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 228–229 | 2 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 242–245 | 4 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 242–243 | 2 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 280–281 | 2 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 284–288 | 5 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 32 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_SplitBlock' range [123-201] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-250] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-273] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [153-271] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [275-297] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-180] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-281] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-288] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [173-174] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [176-177] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [179-186] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-281] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-292] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-109] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-265] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-154] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-158] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-144] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-294] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-227] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-229] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-245] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-243] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-281] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-288] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-299] for track '33' has 1 frames without a visible bounding box.
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

</details>