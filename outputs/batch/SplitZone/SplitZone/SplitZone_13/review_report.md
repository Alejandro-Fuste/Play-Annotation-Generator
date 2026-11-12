# Play-Annotation-Generator Annotation Review — SplitZone_13

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_13`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `22` | `21` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `12` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 7 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `3` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 81 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 82 | START | 82 | 99 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `10` | `10` | 85 | START | 100 | 121 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `16` | `16` | 85 | START | 85 | 181 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `18` | `18` | 85 | START | 85 | 181 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `20` | `20` | 85 | START | 85 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `22` | `21` | 85 | START | 85 | 117 |
| ✅ EXACT | `Action_SplitBlock` | HB | `3` | `3` | 87 | START | 87 | 181 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `4` | 99 | END | 82 | 99 |
| ✅ EXACT | `Action_Handoff` | QB | `4` | `4` | 110 | START | 110 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `10` | `10` | 122 | START | 122 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `12` | `12` | 124 | START | 124 | 241 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 181 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_SnapReceive` | 82 | 99 | 18 | inferred_complete_timeline |
| `Action_None` | 100 | 109 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 110 | 123 | 14 | inferred_complete_timeline |
| `Action_None` | 124 | 267 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_BallCarry` | 124 | 241 | 118 | inferred_complete_timeline |
| `Action_BallCarry` | 244 | 269 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_SplitBlock` | 87 | 181 | 95 | inferred_complete_timeline |
| `Action_None` | 182 | 269 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 269 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 269 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 269 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 181 | 97 | inferred_complete_timeline |
| `Action_None` | 182 | 269 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 181 | 97 | inferred_complete_timeline |
| `Action_None` | 182 | 269 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_BallSnap` | 82 | 99 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 121 | 22 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 122 | 137 | 16 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 143 | 181 | 39 | inferred_complete_timeline |
| `Action_None` | 182 | 269 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 107 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 7–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 84 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 117 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 181 | 60 | inferred_complete_timeline |
| `Action_None` | 182 | 262 | 81 | inferred_complete_timeline |
| `Action_None` | 264 | 269 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 109 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 128 | 47 | inferred_complete_timeline |
| `Action_None` | 130 | 138 | 9 | inferred_complete_timeline |
| `Action_None` | 140 | 220 | 81 | inferred_complete_timeline |
| `Action_None` | 230 | 233 | 4 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |
| `Action_None` | 245 | 262 | 18 | inferred_complete_timeline |
| `Action_None` | 264 | 269 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 111 | 30 | inferred_complete_timeline |
| `Action_None` | 118 | 123 | 6 | inferred_complete_timeline |
| `Action_None` | 128 | 171 | 44 | inferred_complete_timeline |
| `Action_None` | 175 | 182 | 8 | inferred_complete_timeline |
| `Action_None` | 185 | 188 | 4 | inferred_complete_timeline |
| `Action_None` | 190 | 242 | 53 | inferred_complete_timeline |
| `Action_None` | 244 | 269 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 115 | 34 | inferred_complete_timeline |
| `Action_None` | 117 | 149 | 33 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 168 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 117 | 36 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 129 | 148 | 20 | inferred_complete_timeline |
| `Action_None` | 150 | 206 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 125 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 269 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–261
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 261 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 242 | 161 | inferred_complete_timeline |
| `Action_None` | 254 | 259 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 170 | 89 | inferred_complete_timeline |
| `Action_None` | 174 | 178 | 5 | inferred_complete_timeline |
| `Action_None` | 180 | 269 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 269 | 188 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 124–269 | 142 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 132–196 | 63 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 137–168 | 29 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 174–269 | 96 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 182–184 | 3 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 198–269 | 72 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 205–208 | 4 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 216–222 | 6 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 217–269 | 21 | 5 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 224–264 | 31 | 4 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 238–243 | 4 | 2 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 252–269 | 16 | 2 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 252–254 | 3 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 252–255 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `10` (C): Annotated start 85 != Inferred start 100
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [82–99], lower_priority='Action_ZoneBlock' annotated_start=85, effective_Action_ZoneBlock_start=100.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (LG) duration 97 frames exceeds threshold 90 frames [start=85, end=181].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (LT) duration 97 frames exceeds threshold 90 frames [start=85, end=181].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RT) duration 97 frames exceeds threshold 90 frames [start=85, end=181].
- ⚠️ Action 'Action_None' range [82-125] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-109] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-267] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-128] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-220] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-262] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-111] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-171] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-182] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-242] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-170] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-178] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [122-137] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [124-241] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-242] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-259] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-117] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-148] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-206] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-261] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-115] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-149] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-107] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-117] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-262] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-241] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-192] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-158] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-168] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-269] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-219] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-222] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-246] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-259] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-261] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-269] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-255] for track '35' has 1 frames without a visible bounding box.
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