# Play-Annotation-Generator Annotation Review — Draw_13

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_13`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 177
- **Validation Warnings:** 180
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 152
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `19` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `18` | `17` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | RB | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 5 | START | 5 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 5 | START | 5 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 5 | START | 5 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 5 | START | 5 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 5 | START | 5 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `19` | `Group` | 5 | START | 5 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 5 | START | 5 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 5 | START | 5 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `22` | `Group` | 5 | START | 5 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 5 | START | 5 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 5 | START | 5 | 53 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 51 | START | 51 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `14` | `13` | 54 | START | 65 | 77 |
| ✅ EXACT | `Action_PassBlock` | RT | `15` | `14` | 54 | START | 54 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `19` | 54 | START | 54 | 85 |
| ✅ EXACT | `Action_PassBlock` | LG | `21` | `20` | 54 | START | 54 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `4` | `3` | 54 | START | 54 | 92 |
| ✅ EXACT | `Action_SnapReceive` | RB | `18` | `17` | 64 | END | 51 | 64 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | RB | `18` | `17` | 76 | START | 76 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `18` | `17` | 99 | START | 99 | 120 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 154 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 5–299
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 50 | 46 | inferred_complete_timeline |
| `Action_None` | 51 | 121 | 71 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 152 | 25 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 169 | 6 | inferred_complete_timeline |
| `Action_None` | 172 | 193 | 22 | inferred_complete_timeline |
| `Action_None` | 196 | 231 | 36 | inferred_complete_timeline |
| `Action_None` | 233 | 246 | 14 | inferred_complete_timeline |
| `Action_None` | 248 | 255 | 8 | inferred_complete_timeline |
| `Action_None` | 257 | 263 | 7 | inferred_complete_timeline |
| `Action_None` | 267 | 284 | 18 | inferred_complete_timeline |
| `Action_None` | 288 | 299 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 5–227
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 50 | 46 | inferred_complete_timeline |
| `Action_SnapReceive` | 51 | 64 | 14 | inferred_complete_timeline |
| `Action_None` | 65 | 75 | 11 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 76 | 98 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 99 | 120 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 128 | 133 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 164 | 169 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 225 | 227 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 5–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 50 | 46 | inferred_complete_timeline |
| `Action_None` | 51 | 128 | 78 | inferred_complete_timeline |
| `Action_None` | 130 | 170 | 41 | inferred_complete_timeline |
| `Action_None` | 173 | 228 | 56 | inferred_complete_timeline |
| `Action_None` | 232 | 273 | 42 | inferred_complete_timeline |
| `Action_None` | 278 | 299 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 5–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 50 | 46 | inferred_complete_timeline |
| `Action_None` | 51 | 164 | 114 | inferred_complete_timeline |
| `Action_None` | 167 | 169 | 3 | inferred_complete_timeline |
| `Action_None` | 177 | 295 | 119 | inferred_complete_timeline |
| `Action_None` | 299 | 299 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 5–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 50 | 46 | inferred_complete_timeline |
| `Action_None` | 51 | 299 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 5–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 50 | 46 | inferred_complete_timeline |
| `Action_None` | 51 | 121 | 71 | inferred_complete_timeline |
| `Action_None` | 126 | 151 | 26 | inferred_complete_timeline |
| `Action_None` | 165 | 169 | 5 | inferred_complete_timeline |
| `Action_None` | 171 | 262 | 92 | inferred_complete_timeline |
| `Action_None` | 265 | 299 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 5–208
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 53 | 49 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 92 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 99 | 101 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 154 | 52 | inferred_complete_timeline |
| `Action_None` | 155 | 203 | 49 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 5–106
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 53 | 49 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 106 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 5–298
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 50 | 46 | inferred_complete_timeline |
| `Action_BallSnap` | 51 | 64 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 65 | 77 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 108 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 110 | 148 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 151 | 154 | 4 | inferred_complete_timeline |
| `Action_None` | 155 | 169 | 15 | inferred_complete_timeline |
| `Action_None` | 177 | 298 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 5–299
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 53 | 49 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 85 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 112 | 117 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 121 | 123 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 129 | 134 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 139 | 148 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 250 | 86 | inferred_complete_timeline |
| `Action_None` | 252 | 263 | 12 | inferred_complete_timeline |
| `Action_None` | 265 | 299 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 5–99
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 53 | 49 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 99 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 5–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 50 | 46 | inferred_complete_timeline |
| `Action_None` | 51 | 195 | 145 | inferred_complete_timeline |
| `Action_None` | 197 | 211 | 15 | inferred_complete_timeline |
| `Action_None` | 213 | 227 | 15 | inferred_complete_timeline |
| `Action_None` | 237 | 299 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 5–126
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 50 | 46 | inferred_complete_timeline |
| `Action_None` | 51 | 126 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 5–298
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 50 | 46 | inferred_complete_timeline |
| `Action_None` | 51 | 133 | 83 | inferred_complete_timeline |
| `Action_None` | 142 | 147 | 6 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_None` | 182 | 199 | 18 | inferred_complete_timeline |
| `Action_None` | 202 | 223 | 22 | inferred_complete_timeline |
| `Action_None` | 225 | 231 | 7 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 263 | 287 | 25 | inferred_complete_timeline |
| `Action_None` | 289 | 298 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 5–102
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 50 | 46 | inferred_complete_timeline |
| `Action_None` | 51 | 102 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 5–121
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 50 | 46 | inferred_complete_timeline |
| `Action_None` | 51 | 121 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 5–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 50 | 46 | inferred_complete_timeline |
| `Action_None` | 51 | 154 | 104 | inferred_complete_timeline |
| `Action_None` | 160 | 163 | 4 | inferred_complete_timeline |
| `Action_None` | 165 | 299 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 5–118
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 50 | 46 | inferred_complete_timeline |
| `Action_None` | 51 | 118 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 5–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 50 | 46 | inferred_complete_timeline |
| `Action_None` | 51 | 299 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 5–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 50 | 46 | inferred_complete_timeline |
| `Action_None` | 51 | 299 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 5–299
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 50 | 46 | inferred_complete_timeline |
| `Action_None` | 51 | 171 | 121 | inferred_complete_timeline |
| `Action_None` | 177 | 200 | 24 | inferred_complete_timeline |
| `Action_None` | 206 | 209 | 4 | inferred_complete_timeline |
| `Action_None` | 213 | 251 | 39 | inferred_complete_timeline |
| `Action_None` | 254 | 299 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 5–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 50 | 46 | inferred_complete_timeline |
| `Action_None` | 51 | 270 | 220 | inferred_complete_timeline |
| `Action_None` | 275 | 291 | 17 | inferred_complete_timeline |
| `Action_None` | 294 | 295 | 2 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 5–8 | 4 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 26–29 | 4 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 94–299 | 173 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 136–137 | 2 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 136–165 | 30 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 143–217 | 7 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 149–151 | 3 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 168–202 | 24 | 4 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 169–226 | 19 | 5 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 174–299 | 117 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 177–291 | 105 | 5 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 178–260 | 56 | 6 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 191–299 | 97 | 7 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 198–298 | 93 | 5 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 214–298 | 62 | 6 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 226–299 | 64 | 5 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 226–227 | 2 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 242–299 | 50 | 3 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 245–299 | 55 | 1 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 261–299 | 39 | 1 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 293–299 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 134 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [51–64], lower_priority='Action_PassBlock' annotated_start=54, effective_Action_PassBlock_start=65.
- ⚠️ Action 'Action_None' range [51-128] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-170] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-228] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-273] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-121] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-299] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-92] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [99-101] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-203] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-171] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-200] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-209] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-251] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-118] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-154] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-195] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-211] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-227] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-133] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-147] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-199] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-223] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-231] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-287] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-298] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-121] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-151] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-262] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-126] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-270] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-291] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [65-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [80-81] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-108] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [110-148] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-169] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-298] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-99] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [99-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [128-133] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [164-169] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [225-227] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-164] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-295] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-85] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [112-117] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [121-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [129-134] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [139-148] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [150-151] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-250] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-263] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-106] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-121] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-152] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-193] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-231] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-246] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-255] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-263] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-284] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-8] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-29] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-114] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-165] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-147] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-175] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-193] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-198] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-184] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-299] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-251] for track '32' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-280] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-214] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-237] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-260] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-203] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-211] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-247] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-239] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-258] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-271] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-287] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-298] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-239] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-250] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-269] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-287] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-298] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-257] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-250] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '43' has 1 frames without a visible bounding box.
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

</details>