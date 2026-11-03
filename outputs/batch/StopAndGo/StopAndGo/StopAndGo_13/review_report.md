# Play-Annotation-Generator Annotation Review — StopAndGo_13

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_13`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 299
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 145
- **Validation Warnings:** 162
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 124
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_VerticalStem` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_PumpFake` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_SellStop` | WR1 | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `3` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 1 | START | 1 | 7 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `17` | `17` | 4 | START | 8 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `18` | `18` | 4 | START | 4 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 4 | START | 4 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `21` | `21` | 4 | START | 4 | 37 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 7 | END | 1 | 7 |
| ✅ EXACT | `Action_VerticalStem` | WR1 | `0` | `0` | 27 | START | 27 | 48 |
| ✅ EXACT | `Action_PumpFake` | QB | `13` | `13` | 48 | START | 48 | 71 |
| ✅ EXACT | `Action_SellStop` | WR1 | `0` | `0` | 49 | START | 49 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR1 | `0` | `0` | 57 | START | 57 | 168 |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 72 | START | 72 | 80 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 7 | 7 | inferred_complete_timeline |
| `Action_None` | 8 | 47 | 40 | inferred_complete_timeline |
| `Action_PumpFake` | 48 | 71 | 24 | inferred_complete_timeline |
| `Action_ThrowPass` | 72 | 80 | 9 | inferred_complete_timeline |
| `Action_None` | 81 | 153 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 112 | 112 | inferred_complete_timeline |
| `Action_None` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_None` | 127 | 131 | 5 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 51 | 51 | inferred_complete_timeline |
| `Action_None` | 57 | 60 | 4 | inferred_complete_timeline |
| `Action_None` | 63 | 154 | 92 | inferred_complete_timeline |
| `Action_None` | 158 | 162 | 5 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 169 | 299 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_VerticalStem` | 27 | 48 | 22 | inferred_complete_timeline |
| `Action_SellStop` | 49 | 56 | 8 | inferred_complete_timeline |
| `Action_RunGoRoute` | 57 | 168 | 112 | inferred_complete_timeline |
| `Action_RunGoRoute` | 174 | 191 | 18 | inferred_complete_timeline |
| `Action_RunGoRoute` | 194 | 299 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 265 | 265 | inferred_complete_timeline |
| `Action_None` | 267 | 268 | 2 | inferred_complete_timeline |
| `Action_None` | 284 | 294 | 11 | inferred_complete_timeline |
| `Action_None` | 297 | 299 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 82 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 37 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 96 | 100 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 112 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 35 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 42 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 104 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 7 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 79 | 72 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 87 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 108 | 105 | inferred_complete_timeline |
| `Action_PassBlock` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 158 | 162 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 170 | 195 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 96 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 57 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 24 | 24 | inferred_complete_timeline |
| `Action_None` | 28 | 31 | 4 | inferred_complete_timeline |
| `Action_None` | 36 | 39 | 4 | inferred_complete_timeline |
| `Action_None` | 43 | 51 | 9 | inferred_complete_timeline |
| `Action_None` | 57 | 71 | 15 | inferred_complete_timeline |
| `Action_None` | 73 | 112 | 40 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_None` | 117 | 131 | 15 | inferred_complete_timeline |
| `Action_None` | 162 | 166 | 5 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 177 | 4 | inferred_complete_timeline |
| `Action_None` | 179 | 194 | 16 | inferred_complete_timeline |
| `Action_None` | 197 | 241 | 45 | inferred_complete_timeline |
| `Action_None` | 243 | 299 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 54 | 54 | inferred_complete_timeline |
| `Action_None` | 56 | 59 | 4 | inferred_complete_timeline |
| `Action_None` | 68 | 137 | 70 | inferred_complete_timeline |
| `Action_None` | 141 | 144 | 4 | inferred_complete_timeline |
| `Action_None` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_None` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_None` | 181 | 279 | 99 | inferred_complete_timeline |
| `Action_None` | 281 | 282 | 2 | inferred_complete_timeline |
| `Action_None` | 285 | 286 | 2 | inferred_complete_timeline |
| `Action_None` | 288 | 299 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 299 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 108 | 108 | inferred_complete_timeline |
| `Action_None` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_None` | 131 | 133 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 40 | 40 | inferred_complete_timeline |
| `Action_None` | 45 | 92 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 73 | 73 | inferred_complete_timeline |
| `Action_None` | 75 | 197 | 123 | inferred_complete_timeline |
| `Action_None` | 203 | 226 | 24 | inferred_complete_timeline |
| `Action_None` | 245 | 274 | 30 | inferred_complete_timeline |
| `Action_None` | 290 | 299 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 185 | 185 | inferred_complete_timeline |
| `Action_None` | 187 | 299 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 173 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 299 | 299 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–272 | 273 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 50–122 | 73 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 77–193 | 93 | 6 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 91–92 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 99–101 | 3 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 109–111 | 3 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 111–112 | 2 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 119–149 | 29 | 3 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 131–138 | 8 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 148–153 | 6 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 150–151 | 2 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 155–299 | 144 | 2 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 163–164 | 2 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 163–193 | 30 | 2 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 171–173 | 3 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 172–175 | 4 | 1 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 192–226 | 5 | 2 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 194–252 | 59 | 1 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 202–299 | 95 | 2 | Undefined position; Undefined team |
| `40` | `46` | Position_Unknown | Team_Unknown | 210–299 | 79 | 5 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 228–229 | 2 | 1 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 238–264 | 27 | 1 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 265–299 | 35 | 1 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 270–271 | 2 | 1 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 280–283 | 4 | 1 | Undefined position; Undefined team |
| `46` | `63` | Position_Unknown | Team_Unknown | 294–299 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `0` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 106 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 24: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [1–7], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=8.
- ⚠️ Action 'Action_RunGoRoute' range [57-168] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [174-191] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-73] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-197] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-226] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-274] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-112] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-131] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-51] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-60] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-154] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-173] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-57] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-265] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-294] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-40] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-92] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-24] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-31] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-39] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-51] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-71] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-112] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-131] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-194] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-241] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-299] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-54] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-59] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-137] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-279] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-185] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-153] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-96] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [8-79] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [81-87] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-108] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [110-111] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [151-153] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [158-162] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [170-195] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-272] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-35] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-42] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-104] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-37] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [96-100] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-112] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-122] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-131] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-139] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-193] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-122] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-149] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-138] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-153] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-179] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-185] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-193] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-252] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-218] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-240] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-271] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-299] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-264] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-299] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-283] for track '45' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>