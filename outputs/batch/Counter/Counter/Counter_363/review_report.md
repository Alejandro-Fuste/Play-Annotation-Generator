# Play-Annotation-Generator Annotation Review — Counter_363

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_363`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 155
- **Validation Warnings:** 151
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 130
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `9` | `Group` | 0 | START | 0 | 81 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 82 | START | 82 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `17` | `16` | 85 | START | 99 | 159 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `21` | `20` | 85 | START | 85 | 214 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `22` | `21` | 85 | START | 85 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `20` | `19` | 85 | START | 85 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | `3` | `2` | 95 | START | 95 | 141 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 98 | END | 82 | 98 |
| ✅ EXACT | `Action_Handoff` | QB | `16` | `15` | 109 | START | 109 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `3` | 128 | START | 128 | 181 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 214 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_SnapReceive` | 82 | 98 | 17 | inferred_complete_timeline |
| `Action_None` | 99 | 108 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 109 | 127 | 19 | inferred_complete_timeline |
| `Action_None` | 128 | 299 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_BallCarry` | 128 | 181 | 54 | inferred_complete_timeline |
| `Action_BallCarry` | 186 | 188 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 299 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 135 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 95 | 141 | 47 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 143 | 214 | 72 | inferred_complete_timeline |
| `Action_None` | 215 | 237 | 23 | inferred_complete_timeline |
| `Action_None` | 240 | 250 | 11 | inferred_complete_timeline |
| `Action_None` | 253 | 254 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 109 | 28 | inferred_complete_timeline |
| `Action_None` | 111 | 188 | 78 | inferred_complete_timeline |
| `Action_None` | 191 | 219 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 265 | 184 | inferred_complete_timeline |
| `Action_None` | 273 | 274 | 2 | inferred_complete_timeline |
| `Action_None` | 279 | 294 | 16 | inferred_complete_timeline |
| `Action_None` | 296 | 299 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_PullBlock` | 85 | 147 | 63 | inferred_complete_timeline |
| `Action_PullBlock` | 158 | 187 | 30 | inferred_complete_timeline |
| `Action_PullBlock` | 201 | 204 | 4 | inferred_complete_timeline |
| `Action_PullBlock` | 208 | 214 | 7 | inferred_complete_timeline |
| `Action_None` | 215 | 223 | 9 | inferred_complete_timeline |
| `Action_None` | 226 | 232 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_BallSnap` | 82 | 98 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 99 | 159 | 61 | inferred_complete_timeline |
| `Action_DownBlock` | 161 | 174 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 183 | 214 | 32 | inferred_complete_timeline |
| `Action_None` | 215 | 299 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_DownBlock` | 85 | 214 | 130 | inferred_complete_timeline |
| `Action_None` | 215 | 216 | 2 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_None` | 224 | 227 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_DownBlock` | 85 | 124 | 40 | inferred_complete_timeline |
| `Action_DownBlock` | 127 | 130 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 132 | 214 | 83 | inferred_complete_timeline |
| `Action_None` | 215 | 232 | 18 | inferred_complete_timeline |
| `Action_None` | 234 | 299 | 66 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–292
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 172 | 91 | inferred_complete_timeline |
| `Action_None` | 178 | 292 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 107 | 26 | inferred_complete_timeline |
| `Action_None` | 109 | 112 | 4 | inferred_complete_timeline |
| `Action_None` | 130 | 174 | 45 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 179 | 190 | 12 | inferred_complete_timeline |
| `Action_None` | 192 | 299 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 146 | 65 | inferred_complete_timeline |
| `Action_None` | 148 | 154 | 7 | inferred_complete_timeline |
| `Action_None` | 157 | 299 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 113 | 32 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 193 | 112 | inferred_complete_timeline |
| `Action_None` | 195 | 246 | 52 | inferred_complete_timeline |
| `Action_None` | 290 | 292 | 3 | inferred_complete_timeline |
| `Action_None` | 294 | 299 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 160 | 79 | inferred_complete_timeline |
| `Action_None` | 185 | 299 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 299 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 255 | 174 | inferred_complete_timeline |
| `Action_None` | 268 | 299 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 299 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 179 | 98 | inferred_complete_timeline |
| `Action_None` | 193 | 198 | 6 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_None` | 220 | 293 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 116 | 35 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–299 | 251 | 7 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 38–177 | 75 | 10 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 40–194 | 123 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 90–299 | 171 | 12 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 121–140 | 20 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 137–299 | 161 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 139–239 | 99 | 3 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 157–220 | 33 | 4 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 163–164 | 2 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 178–299 | 99 | 5 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 181–299 | 119 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 202–274 | 9 | 2 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 211–217 | 5 | 2 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 216–299 | 45 | 4 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 251–299 | 49 | 1 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 257–259 | 3 | 1 | Undefined position; Undefined team |
| `38` | `63` | Position_Unknown | Team_Unknown | 286–299 | 13 | 2 | Undefined position; Undefined team |
| `39` | `69` | Position_Unknown | Team_Unknown | 295–297 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 109 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '16' (C) duration 130 frames exceeds threshold 90 frames [start=85, end=214].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [82–98], lower_priority='Action_DownBlock' annotated_start=85, effective_Action_DownBlock_start=99.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '19' (LG) duration 130 frames exceeds threshold 90 frames [start=85, end=214].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (RG) duration 130 frames exceeds threshold 90 frames [start=85, end=214].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '21' (RT) duration 130 frames exceeds threshold 90 frames [start=85, end=214].
- ⚠️ Action 'Action_None' range [82-135] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [95-141] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [143-214] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-237] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-250] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [128-181] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [186-188] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-193] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-246] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-255] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-109] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-188] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-219] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-146] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-154] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-299] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-107] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-112] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-174] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-190] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-113] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-179] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-198] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-293] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-172] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-292] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-160] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [99-159] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [161-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-265] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-294] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-116] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [85-147] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [158-187] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [201-204] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-223] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-232] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [85-214] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [85-124] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [127-130] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-232] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-299] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-81] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-99] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-140] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-53] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-71] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-94] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-114] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-126] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-43] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-189] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-92] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-179] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-236] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-260] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-266] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-140] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-165] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-299] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-223] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-239] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-176] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-214] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-220] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-221] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-242] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-281] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-208] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-267] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '39' has 1 frames without a visible bounding box.
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

</details>