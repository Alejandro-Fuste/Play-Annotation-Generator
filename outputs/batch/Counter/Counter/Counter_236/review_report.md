# Play-Annotation-Generator Annotation Review — Counter_236

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_236`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 63
- **Ball Tracks:** 0
- **Action Segments:** 139
- **Validation Warnings:** 204
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 108
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_PullLeadBlock` | TE1 | offense | `10` | `9` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `3` | `2` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `10` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `18` | `Group` | 0 | START | 2 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 106 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 106 | START | 106 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `12` | `11` | 107 | START | 107 | 126 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `13` | `12` | 107 | START | 122 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `16` | `15` | 107 | START | 107 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `8` | `7` | 107 | START | 107 | 162 |
| ✅ EXACT | `Action_PullLeadBlock` | TE1 | `10` | `9` | 107 | START | 107 | 117 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `4` | `3` | 111 | START | 111 | 150 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `2` | 121 | END | 106 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `3` | `2` | 135 | START | 135 | 152 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `4` | `3` | 158 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 231 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_SnapReceive` | 106 | 121 | 16 | inferred_complete_timeline |
| `Action_None` | 122 | 134 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 135 | 152 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 157 | 157 | 1 | inferred_complete_timeline |
| `Action_None` | 158 | 210 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 111 | 150 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 107 | 117 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 2–259
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 101 | 100 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_None` | 111 | 252 | 142 | inferred_complete_timeline |
| `Action_None` | 254 | 259 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 106 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 107 | 143 | 37 | inferred_complete_timeline |
| `Action_DownBlock` | 149 | 231 | 83 | inferred_complete_timeline |
| `Action_None` | 232 | 236 | 5 | inferred_complete_timeline |
| `Action_None` | 241 | 269 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_DownBlock` | 107 | 126 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 134 | 138 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 195 | 196 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_BallSnap` | 106 | 121 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 122 | 140 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_PullBlock` | 107 | 162 | 56 | inferred_complete_timeline |
| `Action_PullBlock` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 195 | 231 | 37 | inferred_complete_timeline |
| `Action_None` | 232 | 258 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–263
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 259 | 154 | inferred_complete_timeline |
| `Action_None` | 261 | 263 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 2–260
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 5 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 8 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 19 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 90 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 95 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 99 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 105 | 1 | inferred_complete_timeline |
| `Action_None` | 106 | 146 | 41 | inferred_complete_timeline |
| `Action_None` | 176 | 208 | 33 | inferred_complete_timeline |
| `Action_None` | 210 | 260 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 204 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–270
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 224 | 119 | inferred_complete_timeline |
| `Action_None` | 228 | 270 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 178 | 73 | inferred_complete_timeline |
| `Action_None` | 204 | 267 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–246
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 241 | 136 | inferred_complete_timeline |
| `Action_None` | 244 | 246 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 134 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–308
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 308 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 266 | 161 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–222 | 164 | 5 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 113–222 | 108 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 125–191 | 65 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 135–247 | 88 | 5 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 143–229 | 46 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 147–277 | 126 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 148–359 | 204 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 168–195 | 11 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 181–182 | 2 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 196–229 | 20 | 3 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 220–222 | 3 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 224–258 | 34 | 2 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 237–262 | 26 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 245–337 | 93 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 251–270 | 20 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 252–357 | 106 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 253–359 | 107 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 255–359 | 103 | 2 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 258–261 | 4 | 1 | Undefined position; Undefined team |
| `36` | `55` | Position_Unknown | Team_Unknown | 276–359 | 84 | 1 | Undefined position; Undefined team |
| `37` | `56` | Position_Unknown | Team_Unknown | 297–300 | 4 | 1 | Undefined position; Undefined team |
| `38` | `57` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |
| `39` | `59` | Position_Unknown | Team_Unknown | 318–352 | 33 | 2 | Undefined position; Undefined team |
| `40` | `61` | Position_Unknown | Team_Unknown | 318–336 | 12 | 3 | Undefined position; Undefined team |
| `41` | `63` | Position_Unknown | Team_Unknown | 319–348 | 27 | 2 | Undefined position; Undefined team |
| `42` | `65` | Position_Unknown | Team_Unknown | 322–324 | 3 | 1 | Undefined position; Undefined team |
| `43` | `66` | Position_Unknown | Team_Unknown | 322–342 | 15 | 3 | Undefined position; Undefined team |
| `44` | `67` | Position_Unknown | Team_Unknown | 323–325 | 3 | 1 | Undefined position; Undefined team |
| `45` | `69` | Position_Unknown | Team_Unknown | 328–331 | 4 | 1 | Undefined position; Undefined team |
| `46` | `70` | Position_Unknown | Team_Unknown | 329–330 | 2 | 1 | Undefined position; Undefined team |
| `47` | `72` | Position_Unknown | Team_Unknown | 330–359 | 29 | 2 | Undefined position; Undefined team |
| `48` | `73` | Position_Unknown | Team_Unknown | 330–336 | 7 | 1 | Undefined position; Undefined team |
| `49` | `75` | Position_Unknown | Team_Unknown | 332–359 | 28 | 1 | Undefined position; Undefined team |
| `50` | `76` | Position_Unknown | Team_Unknown | 334–359 | 22 | 2 | Undefined position; Undefined team |
| `51` | `77` | Position_Unknown | Team_Unknown | 335–359 | 25 | 1 | Undefined position; Undefined team |
| `52` | `78` | Position_Unknown | Team_Unknown | 336–354 | 19 | 1 | Undefined position; Undefined team |
| `53` | `79` | Position_Unknown | Team_Unknown | 336–341 | 6 | 1 | Undefined position; Undefined team |
| `54` | `80` | Position_Unknown | Team_Unknown | 337–359 | 8 | 2 | Undefined position; Undefined team |
| `55` | `82` | Position_Unknown | Team_Unknown | 341–359 | 19 | 1 | Undefined position; Undefined team |
| `56` | `83` | Position_Unknown | Team_Unknown | 341–342 | 2 | 1 | Undefined position; Undefined team |
| `57` | `86` | Position_Unknown | Team_Unknown | 344–353 | 10 | 1 | Undefined position; Undefined team |
| `58` | `87` | Position_Unknown | Team_Unknown | 344–354 | 11 | 1 | Undefined position; Undefined team |
| `59` | `88` | Position_Unknown | Team_Unknown | 348–351 | 4 | 1 | Undefined position; Undefined team |
| `60` | `90` | Position_Unknown | Team_Unknown | 352–359 | 8 | 1 | Undefined position; Undefined team |
| `61` | `91` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |
| `62` | `92` | Position_Unknown | Team_Unknown | 359–359 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (5 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `13` (C): Annotated start 107 != Inferred start 122
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `3` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `4` (RB)

### Track Identity Issues

- ⚠️ 46 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 46 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 92 |
| Missing visible bounding boxes during action | 107 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '3' has invalid range: start=158, end=150. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '7' (RG) duration 125 frames exceeds threshold 90 frames [start=107, end=231].
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [106–121], lower_priority='Action_DownBlock' annotated_start=107, effective_Action_DownBlock_start=122.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '15' (LT) duration 125 frames exceeds threshold 90 frames [start=107, end=231].
- ⚠️ Action 'Action_None' range [106-134] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-241] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [135-152] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [111-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-266] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-178] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-267] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-308] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [107-162] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [180-182] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-258] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-224] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-270] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [107-117] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-204] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [107-126] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [130-132] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [134-138] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [195-196] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [122-140] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-259] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-136] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-154] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-222] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [107-143] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [149-231] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-236] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-269] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-5] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-8] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-19] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-90] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-95] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-99] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-146] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-208] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-260] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-101] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-104] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-252] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-259] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-218] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-186] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-167] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-203] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-247] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-186] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-190] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-204] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-277] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-204] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-223] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-195] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-199] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-229] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-248] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-258] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-262] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-337] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-270] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-357] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-344] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-300] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-325] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-352] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-324] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-336] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-324] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-348] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-324] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-330] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-342] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-331] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-336] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-359] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-342] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-359] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-359] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-354] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-341] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-340] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-353] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-354] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-351] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.

</details>