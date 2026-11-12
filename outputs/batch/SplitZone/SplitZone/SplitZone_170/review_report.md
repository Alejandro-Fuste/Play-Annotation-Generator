# Play-Annotation-Generator Annotation Review — SplitZone_170

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_170`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 74
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | offense | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `10` | `10` |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | C | offense | `9` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `11` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 67 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `9` | 68 | START | 68 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `12` | `12` | 71 | START | 71 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `13` | 71 | START | 71 | 82 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `2` | 71 | START | 71 | 152 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `7` | 71 | START | 71 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `9` | `9` | 71 | START | 85 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | `11` | `11` | 76 | START | 76 | 77 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 84 | END | 68 | 84 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 94 | START | 94 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `10` | `10` | 101 | START | 101 | 153 |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | C | `9` | `9` | 121 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 154 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_SnapReceive` | 68 | 84 | 17 | inferred_complete_timeline |
| `Action_None` | 85 | 93 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 94 | 100 | 7 | inferred_complete_timeline |
| `Action_None` | 101 | 101 | 1 | inferred_complete_timeline |
| `Action_None` | 109 | 132 | 24 | inferred_complete_timeline |
| `Action_None` | 136 | 144 | 9 | inferred_complete_timeline |
| `Action_None` | 155 | 162 | 8 | inferred_complete_timeline |
| `Action_None` | 177 | 247 | 71 | inferred_complete_timeline |
| `Action_None` | 256 | 264 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_BallCarry` | 101 | 153 | 53 | inferred_complete_timeline |
| `Action_BallCarry` | 186 | 187 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_SplitBlock` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_SplitBlock` | 80 | 82 | 3 | inferred_complete_timeline |
| `Action_SplitBlock` | 84 | 91 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 152 | 82 | inferred_complete_timeline |
| `Action_None` | 165 | 247 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 107 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 119 | 154 | 36 | inferred_complete_timeline |
| `Action_None` | 155 | 258 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_BallSnap` | 68 | 84 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 93 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 99 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–282
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 82 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 114 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 154 | 26 | inferred_complete_timeline |
| `Action_None` | 155 | 282 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 111 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 197 | 130 | inferred_complete_timeline |
| `Action_None` | 201 | 299 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 67 | 1 | inferred_complete_timeline |
| `Action_None` | 68 | 107 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 209 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 160 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 181 | 114 | inferred_complete_timeline |
| `Action_None` | 183 | 232 | 50 | inferred_complete_timeline |
| `Action_None` | 234 | 299 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 147 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 229 | 162 | inferred_complete_timeline |
| `Action_None` | 231 | 234 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 97–272 | 176 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 122–299 | 142 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 125–233 | 109 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 136–260 | 125 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 146–299 | 151 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 160–163 | 4 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 168–299 | 132 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 169–299 | 130 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 213–254 | 42 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 220–267 | 48 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 230–232 | 3 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 248–299 | 52 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 297–299 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (2 segments found)
- ❌ Missing segment for action `Action_BlockSecondLevel` on target `9` (C)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 45 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_BlockSecondLevel' for track '9' has invalid range: start=121, end=99. Clamping end to start.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [68–84], lower_priority='Action_ZoneBlock' annotated_start=71, effective_Action_ZoneBlock_start=85.
- ⚠️ Action 'Action_None' range [68-181] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-232] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-299] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-229] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-152] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-247] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-197] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-107] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-209] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-160] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-111] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '8' starts at frame 101, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [101-101] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-132] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-144] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-162] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-247] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-264] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-93] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-99] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [101-153] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [186-187] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [76-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [80-82] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [84-91] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-107] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-258] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-82] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-114] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-125] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-282] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-147] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-272] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-233] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-260] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-169] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-195] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-254] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-267] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '25' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.

</details>