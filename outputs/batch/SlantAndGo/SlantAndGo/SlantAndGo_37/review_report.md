# Play-Annotation-Generator Annotation Review — SlantAndGo_37

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_37`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 133
- **Validation Warnings:** 127
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
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 112
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | QB | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | OLB | defense | `18` | `18` |
| ✅ EXACT | `Action_SellRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_VerticalStem` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | OLB | defense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `12` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `14` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 24 |
| ✅ EXACT | `Action_BallSnap` | QB | `17` | `17` | 22 | START | 22 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `15` | `15` | 25 | START | 25 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `16` | `16` | 25 | START | 25 | 148 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `19` | `19` | 25 | START | 25 | 60 |
| ✅ EXACT | `Action_PassBlock` | RG | `21` | `21` | 25 | START | 25 | 230 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `4` | `4` | 25 | START | 25 | 227 |
| ✅ EXACT | `Action_SnapReceive` | OLB | `18` | `18` | 35 | END | 22 | 35 |
| ✅ EXACT | `Action_SellRoute` | WR2 | `1` | `1` | 58 | START | 58 | 90 |
| ✅ EXACT | `Action_VerticalStem` | WR2 | `1` | `1` | 91 | START | 91 | 207 |
| ✅ EXACT | `Action_ThrowPass` | OLB | `18` | `18` | 111 | START | 111 | 121 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_BallSnap` | 22 | 35 | 14 | inferred_complete_timeline |
| `Action_None` | 36 | 42 | 7 | inferred_complete_timeline |
| `Action_None` | 44 | 90 | 47 | inferred_complete_timeline |
| `Action_None` | 100 | 133 | 34 | inferred_complete_timeline |
| `Action_None` | 137 | 142 | 6 | inferred_complete_timeline |
| `Action_None` | 147 | 153 | 7 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 168 | 4 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 177 | 4 | inferred_complete_timeline |
| `Action_None` | 188 | 190 | 3 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_None` | 197 | 199 | 3 | inferred_complete_timeline |
| `Action_None` | 206 | 232 | 27 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 239 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 155 | 134 | inferred_complete_timeline |
| `Action_None` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_None` | 162 | 173 | 12 | inferred_complete_timeline |
| `Action_None` | 185 | 188 | 4 | inferred_complete_timeline |
| `Action_None` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_None` | 195 | 239 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 175 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_SellRoute` | 58 | 90 | 33 | inferred_complete_timeline |
| `Action_VerticalStem` | 91 | 207 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 214 | 193 | inferred_complete_timeline |
| `Action_None` | 217 | 220 | 4 | inferred_complete_timeline |
| `Action_None` | 226 | 229 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 90 | 69 | inferred_complete_timeline |
| `Action_None` | 96 | 239 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 227 | 203 | inferred_complete_timeline |
| `Action_PassBlock` | 229 | 239 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 124 | 100 | inferred_complete_timeline |
| `Action_PassBlock` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 190 | 199 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 215 | 218 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 148 | 124 | inferred_complete_timeline |
| `Action_PassBlock` | 152 | 165 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 230 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 60 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 74 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 86 | 89 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 91 | 108 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 110 | 134 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 138 | 148 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 152 | 178 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 183 | 190 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 57 | 36 | inferred_complete_timeline |
| `Action_None` | 70 | 86 | 17 | inferred_complete_timeline |
| `Action_None` | 91 | 169 | 79 | inferred_complete_timeline |
| `Action_None` | 175 | 177 | 3 | inferred_complete_timeline |
| `Action_None` | 180 | 195 | 16 | inferred_complete_timeline |
| `Action_None` | 197 | 199 | 3 | inferred_complete_timeline |
| `Action_None` | 204 | 219 | 16 | inferred_complete_timeline |
| `Action_None` | 221 | 239 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 96 | 75 | inferred_complete_timeline |
| `Action_None` | 100 | 104 | 5 | inferred_complete_timeline |
| `Action_None` | 108 | 114 | 7 | inferred_complete_timeline |
| `Action_None` | 122 | 159 | 38 | inferred_complete_timeline |
| `Action_None` | 165 | 234 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 222 | 201 | inferred_complete_timeline |
| `Action_None` | 226 | 239 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 172 | 151 | inferred_complete_timeline |
| `Action_None` | 174 | 192 | 19 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 22 | 35 | 14 | inferred_complete_timeline |
| `Action_None` | 36 | 110 | 75 | inferred_complete_timeline |
| `Action_ThrowPass` | 111 | 121 | 11 | inferred_complete_timeline |
| `Action_None` | 122 | 229 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 89 | 68 | inferred_complete_timeline |
| `Action_None` | 96 | 104 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 171 | 150 | inferred_complete_timeline |
| `Action_None` | 175 | 194 | 20 | inferred_complete_timeline |
| `Action_None` | 199 | 211 | 13 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 223 | 7 | inferred_complete_timeline |
| `Action_None` | 225 | 235 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 169 | 148 | inferred_complete_timeline |
| `Action_None` | 171 | 174 | 4 | inferred_complete_timeline |
| `Action_None` | 180 | 239 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 105–109 | 5 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 130–156 | 22 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 140–141 | 2 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 164–239 | 61 | 4 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 174–239 | 60 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 184–210 | 13 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 186–234 | 42 | 4 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 215–219 | 5 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 223–238 | 16 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 223–224 | 2 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 224–239 | 16 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 229–237 | 7 | 2 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 233–234 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (10 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 100 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [22-175] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [91-207] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-96] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-104] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-114] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-159] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-234] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-169] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-227] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [229-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-57] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-86] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-195] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-219] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-239] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-172] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-192] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-171] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-194] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-211] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-223] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-235] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-222] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-239] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-155] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-173] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-214] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-220] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-90] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-124] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [126-127] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [190-199] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [215-218] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-148] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [152-165] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-42] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-90] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-133] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-142] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-153] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-232] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-229] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-60] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-74] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [76-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [86-89] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [91-108] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [110-134] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [138-148] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [152-178] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [180-181] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [183-190] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-89] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-104] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-230] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-109] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-138] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-147] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-188] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-220] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-239] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-189] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-234] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-238] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-239] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '34' has 1 frames without a visible bounding box.
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

</details>