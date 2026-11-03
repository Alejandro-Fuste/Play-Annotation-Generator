# Play-Annotation-Generator Annotation Review — Slants0to10_13

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_13`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 157
- **Validation Warnings:** 165
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 136
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `20` | `20` |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 2 | START | 2 | 17 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `14` | `14` | 5 | START | 18 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `17` | `17` | 5 | START | 5 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `18` | `18` | 5 | START | 5 | 85 |
| ✅ EXACT | `Action_PassBlock` | LG | `19` | `19` | 5 | START | 5 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `20` | `20` | 5 | START | 5 | 46 |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | `3` | `3` | 16 | START | 16 | 78 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 17 | END | 2 | 17 |
| ✅ EXACT | `Action_ThrowPass` | QB | `15` | `15` | 64 | START | 64 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `3` | `3` | 106 | START | 106 | 157 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 2 | 17 | 16 | inferred_complete_timeline |
| `Action_None` | 18 | 63 | 46 | inferred_complete_timeline |
| `Action_ThrowPass` | 64 | 73 | 10 | inferred_complete_timeline |
| `Action_None` | 74 | 162 | 89 | inferred_complete_timeline |
| `Action_None` | 165 | 190 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 85 | 84 | inferred_complete_timeline |
| `Action_None` | 87 | 158 | 72 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 299 | 298 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 16 | 78 | 63 | inferred_complete_timeline |
| `Action_None` | 79 | 105 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 106 | 157 | 52 | inferred_complete_timeline |
| `Action_BallCarry` | 160 | 161 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 208 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 299 | 298 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 46 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 67 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 72 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 87 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 108 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 111 | 130 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 132 | 134 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 136 | 139 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 141 | 145 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 154 | 158 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 160 | 162 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 190 | 194 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–21
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 21 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 2 | 17 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 72 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 85 | 81 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 98 | 103 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 105 | 108 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 108 | 104 | inferred_complete_timeline |
| `Action_PassBlock` | 110 | 202 | 93 | inferred_complete_timeline |
| `Action_PassBlock` | 216 | 223 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 236 | 259 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 261 | 263 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 266 | 299 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 56 | 55 | inferred_complete_timeline |
| `Action_None` | 62 | 72 | 11 | inferred_complete_timeline |
| `Action_None` | 80 | 84 | 5 | inferred_complete_timeline |
| `Action_None` | 95 | 100 | 6 | inferred_complete_timeline |
| `Action_None` | 102 | 108 | 7 | inferred_complete_timeline |
| `Action_None` | 111 | 117 | 7 | inferred_complete_timeline |
| `Action_None` | 121 | 130 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–56
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 50 | 49 | inferred_complete_timeline |
| `Action_None` | 55 | 56 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 53 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 234 | 233 | inferred_complete_timeline |
| `Action_None` | 239 | 294 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–272
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 87 | 86 | inferred_complete_timeline |
| `Action_None` | 90 | 112 | 23 | inferred_complete_timeline |
| `Action_None` | 115 | 117 | 3 | inferred_complete_timeline |
| `Action_None` | 121 | 139 | 19 | inferred_complete_timeline |
| `Action_None` | 144 | 165 | 22 | inferred_complete_timeline |
| `Action_None` | 172 | 175 | 4 | inferred_complete_timeline |
| `Action_None` | 182 | 195 | 14 | inferred_complete_timeline |
| `Action_None` | 198 | 222 | 25 | inferred_complete_timeline |
| `Action_None` | 224 | 234 | 11 | inferred_complete_timeline |
| `Action_None` | 270 | 272 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 124 | 123 | inferred_complete_timeline |
| `Action_None` | 126 | 154 | 29 | inferred_complete_timeline |
| `Action_None` | 156 | 246 | 91 | inferred_complete_timeline |
| `Action_None` | 254 | 259 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 299 | 298 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 164 | 163 | inferred_complete_timeline |
| `Action_None` | 166 | 170 | 5 | inferred_complete_timeline |
| `Action_None` | 172 | 176 | 5 | inferred_complete_timeline |
| `Action_None` | 180 | 185 | 6 | inferred_complete_timeline |
| `Action_None` | 208 | 212 | 5 | inferred_complete_timeline |
| `Action_None` | 219 | 222 | 4 | inferred_complete_timeline |
| `Action_None` | 224 | 239 | 16 | inferred_complete_timeline |
| `Action_None` | 282 | 286 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 152 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 61 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 195 | 194 | inferred_complete_timeline |
| `Action_None` | 214 | 271 | 58 | inferred_complete_timeline |
| `Action_None` | 274 | 275 | 2 | inferred_complete_timeline |
| `Action_None` | 280 | 284 | 5 | inferred_complete_timeline |
| `Action_None` | 291 | 299 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 57–60 | 4 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 67–107 | 21 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 72–79 | 8 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 83–299 | 208 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 89–299 | 205 | 4 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 98–299 | 144 | 9 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 122–123 | 2 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 122–299 | 129 | 3 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 150–299 | 147 | 3 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 153–155 | 3 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 161–299 | 136 | 4 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 163–239 | 60 | 3 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 166–169 | 4 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 173–195 | 17 | 3 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 175–299 | 110 | 3 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 192–258 | 61 | 2 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 193–194 | 2 | 1 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 197–299 | 103 | 1 | Undefined position; Undefined team |
| `40` | `45` | Position_Unknown | Team_Unknown | 213–299 | 81 | 2 | Undefined position; Undefined team |
| `41` | `46` | Position_Unknown | Team_Unknown | 275–287 | 12 | 2 | Undefined position; Undefined team |
| `42` | `47` | Position_Unknown | Team_Unknown | 281–288 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `14` (C): Annotated start 5 != Inferred start 18
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (13 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 120 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [2–17], lower_priority='Action_PassBlock' annotated_start=5, effective_Action_PassBlock_start=18.
- ⚠️ Action 'Action_None' range [2-208] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-50] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-56] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [106-157] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [160-161] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-152] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-195] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-271] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-284] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-56] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-72] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-84] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-100] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-108] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-117] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-130] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-87] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-112] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-139] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-165] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-195] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-222] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-234] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-61] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-234] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-294] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-53] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-164] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-185] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-212] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-239] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-286] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-124] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-154] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-246] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-259] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-72] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-162] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-190] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-108] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [110-202] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [216-223] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [236-259] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [261-263] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [266-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-85] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-96] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [98-103] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [105-108] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-21] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-46] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-67] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-72] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-87] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-108] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [111-130] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [132-134] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [136-139] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [141-145] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [154-158] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [160-162] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [172-173] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [190-194] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-85] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-158] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-60] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-76] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-85] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-79] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-299] for track '25' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-164] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-280] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-110] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-144] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-284] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-190] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-161] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-299] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-166] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-244] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-286] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-197] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-239] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-185] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-195] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-251] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-248] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-299] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-284] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-288] for track '42' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>