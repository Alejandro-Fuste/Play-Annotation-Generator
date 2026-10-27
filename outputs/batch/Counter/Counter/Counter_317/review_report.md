# Play-Annotation-Generator Annotation Review — Counter_317

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_317`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 160
- **Validation Warnings:** 177
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
- **Inferred Coverage Segments (Action_None):** 133
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `9` | `Group` | 0 | START | 0 | 81 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 82 | START | 82 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `19` | `18` | 85 | START | 85 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `20` | `19` | 85 | START | 85 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `21` | `20` | 85 | START | 98 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `13` | `12` | 85 | START | 85 | 159 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `22` | `21` | 85 | START | 85 | 159 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 97 | END | 82 | 97 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `10` | 113 | START | 113 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `15` | `14` | 133 | START | 133 | 261 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 187 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–351
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_SnapReceive` | 82 | 97 | 16 | inferred_complete_timeline |
| `Action_None` | 98 | 112 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 113 | 132 | 20 | inferred_complete_timeline |
| `Action_None` | 133 | 351 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 132 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 133 | 261 | 129 | inferred_complete_timeline |
| `Action_BallCarry` | 264 | 359 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 232 | 151 | inferred_complete_timeline |
| `Action_None` | 234 | 236 | 3 | inferred_complete_timeline |
| `Action_None` | 239 | 243 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 359 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 113 | 32 | inferred_complete_timeline |
| `Action_None` | 117 | 128 | 12 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_None` | 156 | 159 | 4 | inferred_complete_timeline |
| `Action_None` | 162 | 164 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 359 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_DownBlock` | 85 | 104 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–270
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_DownBlock` | 85 | 102 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 109 | 111 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 118 | 121 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 125 | 128 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 131 | 133 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 138 | 154 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 157 | 166 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 183 | 184 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_None` | 237 | 258 | 22 | inferred_complete_timeline |
| `Action_None` | 268 | 270 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–292
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_BallSnap` | 82 | 97 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 98 | 128 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 141 | 187 | 47 | inferred_complete_timeline |
| `Action_None` | 188 | 191 | 4 | inferred_complete_timeline |
| `Action_None` | 194 | 272 | 79 | inferred_complete_timeline |
| `Action_None` | 277 | 292 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_PullBlock` | 85 | 159 | 75 | inferred_complete_timeline |
| `Action_PullBlock` | 164 | 179 | 16 | inferred_complete_timeline |
| `Action_PullBlock` | 184 | 187 | 4 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 201 | 11 | inferred_complete_timeline |
| `Action_None` | 204 | 208 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 85 | 159 | 75 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 162 | 164 | 3 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 176 | 187 | 12 | inferred_complete_timeline |
| `Action_None` | 188 | 204 | 17 | inferred_complete_timeline |
| `Action_None` | 206 | 216 | 11 | inferred_complete_timeline |
| `Action_None` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_None` | 227 | 237 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 118 | 37 | inferred_complete_timeline |
| `Action_None` | 133 | 143 | 11 | inferred_complete_timeline |
| `Action_None` | 145 | 147 | 3 | inferred_complete_timeline |
| `Action_None` | 154 | 156 | 3 | inferred_complete_timeline |
| `Action_None` | 159 | 162 | 4 | inferred_complete_timeline |
| `Action_None` | 173 | 359 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 109 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 126 | 45 | inferred_complete_timeline |
| `Action_None` | 128 | 136 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 182 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 139 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 180 | 99 | inferred_complete_timeline |
| `Action_None` | 187 | 189 | 3 | inferred_complete_timeline |
| `Action_None` | 191 | 208 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 359 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 359 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 263 | 182 | inferred_complete_timeline |
| `Action_None` | 265 | 267 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–342
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 190 | 109 | inferred_complete_timeline |
| `Action_None` | 198 | 263 | 66 | inferred_complete_timeline |
| `Action_None` | 267 | 320 | 54 | inferred_complete_timeline |
| `Action_None` | 322 | 342 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–359 | 350 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 112–359 | 235 | 5 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 132–133 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 144–148 | 5 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 157–173 | 17 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 158–169 | 10 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 171–175 | 5 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 176–359 | 179 | 4 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 196–359 | 163 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 204–359 | 141 | 4 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 209–359 | 134 | 3 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 220–359 | 121 | 7 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 253–255 | 3 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 256–259 | 4 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 265–359 | 93 | 2 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 269–359 | 86 | 2 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 272–359 | 87 | 2 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 282–359 | 53 | 6 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 287–320 | 7 | 2 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 289–343 | 38 | 7 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 308–359 | 51 | 2 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 312–317 | 6 | 1 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 316–359 | 44 | 1 | Undefined position; Undefined team |
| `44` | `63` | Position_Unknown | Team_Unknown | 331–359 | 16 | 3 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 350–359 | 10 | 1 | Undefined position; Undefined team |
| `46` | `67` | Position_Unknown | Team_Unknown | 359–359 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (10 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `22` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 119 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 636: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '12' (RG) duration 103 frames exceeds threshold 90 frames [start=85, end=187].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '18' (LG) duration 103 frames exceeds threshold 90 frames [start=85, end=187].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (C) duration 103 frames exceeds threshold 90 frames [start=85, end=187].
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [82–97], lower_priority='Action_DownBlock' annotated_start=85, effective_Action_DownBlock_start=98.
- ⚠️ Action 'Action_None' range [82-232] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-204] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-359] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-126] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-136] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-263] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-208] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-113] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-128] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-139] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-351] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-118] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-143] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-359] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [85-159] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [164-179] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-201] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-182] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-122] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [133-261] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [264-359] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-190] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-263] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-320] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-342] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-109] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-359] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [85-102] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [109-111] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [118-121] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [125-128] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [131-133] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [138-154] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [157-166] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [172-173] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [183-184] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-258] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-270] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [85-104] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [98-128] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [130-131] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [141-187] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-272] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-292] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [85-159] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [162-164] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [167-168] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-204] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-216] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-237] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-119] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-353] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-148] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-173] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-175] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-195] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-230] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-263] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-351] for track '29' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-262] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-274] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-359] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-270] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-280] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-359] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-250] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-294] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-304] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-353] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-259] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-269] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-353] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-277] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-303] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-310] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-325] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-347] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-291] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-300] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-324] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-329] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-337] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-310] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-359] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-317] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-359] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-333] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-348] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-359] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>