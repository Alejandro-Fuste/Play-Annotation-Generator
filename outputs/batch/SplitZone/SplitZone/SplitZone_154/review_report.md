# Play-Annotation-Generator Annotation Review — SplitZone_154

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_154`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 111
- **Validation Warnings:** 126
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_SplitBlock` | TE1 | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LB1 | defense | `7` | `7` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `10` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 9 | START | 10 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 9 | START | 10 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 9 | START | 10 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 9 | START | 10 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 9 | START | 10 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 9 | START | 10 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 9 | START | 10 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 9 | START | 10 | 88 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 86 | START | 86 | 91 |
| ✅ EXACT | `Action_SplitBlock` | TE1 | `6` | `6` | 89 | START | 89 | 157 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `1` | `1` | 89 | START | 89 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `15` | 89 | START | 103 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `3` | `3` | 89 | START | 89 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `9` | `9` | 89 | START | 89 | 97 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 97 | END | 86 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LB1 | `7` | `7` | 125 | START | 125 | 141 |
| ✅ EXACT | `Action_BallCarry` | QB | `10` | `10` | 143 | START | 143 | 159 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 207 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 10–159
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 85 | 76 | inferred_complete_timeline |
| `Action_SnapReceive` | 86 | 97 | 12 | inferred_complete_timeline |
| `Action_None` | 98 | 142 | 45 | inferred_complete_timeline |
| `Action_BallCarry` | 143 | 159 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 10–141
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 85 | 76 | inferred_complete_timeline |
| `Action_None` | 86 | 141 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 10–157
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 88 | 79 | inferred_complete_timeline |
| `Action_SplitBlock` | 89 | 157 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 10–136
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 85 | 76 | inferred_complete_timeline |
| `Action_None` | 86 | 136 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 10–262
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 88 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 130 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 149 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 207 | 53 | inferred_complete_timeline |
| `Action_None` | 208 | 217 | 10 | inferred_complete_timeline |
| `Action_None` | 223 | 262 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 10–299
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 41 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 44 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 85 | 39 | inferred_complete_timeline |
| `Action_BallSnap` | 86 | 91 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 137 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 160 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 207 | 18 | inferred_complete_timeline |
| `Action_None` | 212 | 233 | 22 | inferred_complete_timeline |
| `Action_None` | 238 | 299 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 10–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 88 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 124 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 207 | 80 | inferred_complete_timeline |
| `Action_None` | 208 | 216 | 9 | inferred_complete_timeline |
| `Action_None` | 218 | 259 | 42 | inferred_complete_timeline |
| `Action_None` | 261 | 299 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 10–178
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 88 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 97 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 106 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 152 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 178 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 10–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 85 | 76 | inferred_complete_timeline |
| `Action_None` | 86 | 137 | 52 | inferred_complete_timeline |
| `Action_None` | 143 | 145 | 3 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 158 | 299 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 10–141
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 85 | 76 | inferred_complete_timeline |
| `Action_None` | 86 | 141 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 10–187
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 85 | 76 | inferred_complete_timeline |
| `Action_None` | 86 | 93 | 8 | inferred_complete_timeline |
| `Action_None` | 142 | 144 | 3 | inferred_complete_timeline |
| `Action_None` | 180 | 187 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 10–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 85 | 76 | inferred_complete_timeline |
| `Action_None` | 86 | 99 | 14 | inferred_complete_timeline |
| `Action_None` | 106 | 116 | 11 | inferred_complete_timeline |
| `Action_None` | 120 | 290 | 171 | inferred_complete_timeline |
| `Action_None` | 294 | 299 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 10–289
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 114 | 105 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 124 | 8 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 125 | 141 | 17 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 143 | 161 | 19 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 167 | 207 | 41 | inferred_complete_timeline |
| `Action_None` | 208 | 237 | 30 | inferred_complete_timeline |
| `Action_None` | 244 | 289 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 10–96
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 85 | 76 | inferred_complete_timeline |
| `Action_None` | 86 | 92 | 7 | inferred_complete_timeline |
| `Action_None` | 94 | 96 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 10–299
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 85 | 76 | inferred_complete_timeline |
| `Action_None` | 86 | 101 | 16 | inferred_complete_timeline |
| `Action_None` | 130 | 147 | 18 | inferred_complete_timeline |
| `Action_None` | 158 | 177 | 20 | inferred_complete_timeline |
| `Action_None` | 179 | 299 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 10–162
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 85 | 76 | inferred_complete_timeline |
| `Action_None` | 86 | 162 | 77 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 64–125 | 62 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 94–151 | 42 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 111–164 | 52 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 114–200 | 78 | 5 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 142–299 | 154 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 145–181 | 37 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 154–258 | 100 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 178–188 | 8 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 187–209 | 23 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 190–299 | 110 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 192–199 | 8 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 208–292 | 58 | 4 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 214–299 | 70 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 215–298 | 82 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 217–299 | 81 | 3 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 232–299 | 65 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 234–299 | 59 | 3 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 287–299 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `7` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 85 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (RG) duration 119 frames exceeds threshold 90 frames [start=89, end=207].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (LT) duration 119 frames exceeds threshold 90 frames [start=89, end=207].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (C) duration 119 frames exceeds threshold 90 frames [start=89, end=207].
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [86–97], lower_priority='Action_ZoneBlock' annotated_start=89, effective_Action_ZoneBlock_start=98.
- ⚠️ Action 'Action_None' range [86-101] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-147] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-177] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-124] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [128-207] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-216] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-259] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-299] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-162] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-130] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-149] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [155-207] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-217] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-262] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-136] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-137] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [89-157] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-114] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [125-141] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [143-161] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [167-207] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-289] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-99] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-116] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-290] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-97] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-152] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [154-155] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [164-178] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [143-159] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-92] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-141] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-141] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-93] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-187] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-41] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-44] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-85] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [86-91] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-137] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [144-160] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-207] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-233] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-125] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-119] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-151] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-159] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-130] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-157] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-193] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-153] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-235] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-181] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-165] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-258] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-182] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-209] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-199] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-246] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-270] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-288] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-228] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-298] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-230] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-292] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-268] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-299] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-265] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-299] for track '32' has 1 frames without a visible bounding box.
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