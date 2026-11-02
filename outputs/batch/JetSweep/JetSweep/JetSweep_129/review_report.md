# Play-Annotation-Generator Annotation Review — JetSweep_129

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_129`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 135
- **Validation Warnings:** 129
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 106
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `2` | `1` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | SAF1 | defense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Toss` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 88 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `2` | `1` | 56 | START | 56 | 119 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 89 | START | 89 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | SAF1 | `19` | `18` | 91 | START | 91 | 183 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `10` | `9` | 91 | START | 91 | 200 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `12` | `11` | 91 | START | 91 | 200 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `15` | `14` | 91 | START | 91 | 200 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `18` | `17` | 91 | START | 91 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `22` | `21` | 91 | START | 105 | 109 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 104 | END | 89 | 104 |
| ✅ EXACT | `Action_Toss` | QB | `6` | `5` | 111 | START | 111 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `2` | `1` | 120 | START | 120 | 233 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 200 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_SnapReceive` | 89 | 104 | 16 | inferred_complete_timeline |
| `Action_None` | 105 | 110 | 6 | inferred_complete_timeline |
| `Action_Toss` | 111 | 119 | 9 | inferred_complete_timeline |
| `Action_None` | 120 | 186 | 67 | inferred_complete_timeline |
| `Action_None` | 188 | 194 | 7 | inferred_complete_timeline |
| `Action_None` | 198 | 216 | 19 | inferred_complete_timeline |
| `Action_None` | 219 | 299 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 189 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_JetMotion` | 56 | 119 | 64 | inferred_complete_timeline |
| `Action_BallCarry` | 120 | 233 | 114 | inferred_complete_timeline |
| `Action_BallCarry` | 235 | 250 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 255 | 256 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 260 | 299 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 140 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 168 | 80 | inferred_complete_timeline |
| `Action_None` | 171 | 299 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 299 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 200 | 110 | inferred_complete_timeline |
| `Action_None` | 201 | 299 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 200 | 110 | inferred_complete_timeline |
| `Action_None` | 201 | 299 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_BallSnap` | 89 | 104 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 105 | 109 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 122 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 127 | 200 | 74 | inferred_complete_timeline |
| `Action_None` | 201 | 258 | 58 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_None` | 273 | 299 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 200 | 110 | inferred_complete_timeline |
| `Action_None` | 201 | 268 | 68 | inferred_complete_timeline |
| `Action_None` | 282 | 299 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 200 | 110 | inferred_complete_timeline |
| `Action_None` | 201 | 227 | 27 | inferred_complete_timeline |
| `Action_None` | 232 | 235 | 4 | inferred_complete_timeline |
| `Action_None` | 237 | 299 | 63 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 118 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 204 | 116 | inferred_complete_timeline |
| `Action_None` | 208 | 212 | 5 | inferred_complete_timeline |
| `Action_None` | 214 | 235 | 22 | inferred_complete_timeline |
| `Action_None` | 243 | 244 | 2 | inferred_complete_timeline |
| `Action_None` | 248 | 299 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 169 | 81 | inferred_complete_timeline |
| `Action_None` | 171 | 181 | 11 | inferred_complete_timeline |
| `Action_None` | 183 | 188 | 6 | inferred_complete_timeline |
| `Action_None` | 190 | 210 | 21 | inferred_complete_timeline |
| `Action_None` | 212 | 217 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 114 | 26 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 299 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 151 | 63 | inferred_complete_timeline |
| `Action_None` | 155 | 199 | 45 | inferred_complete_timeline |
| `Action_None` | 242 | 259 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 179 | 91 | inferred_complete_timeline |
| `Action_None` | 181 | 208 | 28 | inferred_complete_timeline |
| `Action_None` | 214 | 216 | 3 | inferred_complete_timeline |
| `Action_None` | 222 | 223 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–256
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 190 | 102 | inferred_complete_timeline |
| `Action_None` | 197 | 219 | 23 | inferred_complete_timeline |
| `Action_None` | 227 | 256 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–270
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 191 | 103 | inferred_complete_timeline |
| `Action_None` | 193 | 262 | 70 | inferred_complete_timeline |
| `Action_None` | 266 | 270 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_LeadBlock` | 91 | 183 | 93 | inferred_complete_timeline |
| `Action_LeadBlock` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_LeadBlock` | 189 | 200 | 12 | inferred_complete_timeline |
| `Action_None` | 201 | 299 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–290
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 260 | 172 | inferred_complete_timeline |
| `Action_None` | 266 | 273 | 8 | inferred_complete_timeline |
| `Action_None` | 276 | 280 | 5 | inferred_complete_timeline |
| `Action_None` | 286 | 290 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 126–193 | 23 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 137–299 | 146 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 145–149 | 5 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 149–197 | 49 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 156–256 | 83 | 5 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 160–299 | 132 | 4 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 171–232 | 51 | 5 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 203–204 | 2 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 223–237 | 15 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 240–299 | 60 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 240–242 | 3 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 243–299 | 37 | 7 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 253–299 | 46 | 2 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 273–275 | 3 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 283–298 | 13 | 3 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 289–299 | 11 | 1 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 296–299 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 87 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (LT) duration 110 frames exceeds threshold 90 frames [start=91, end=200].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (RT) duration 110 frames exceeds threshold 90 frames [start=91, end=200].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (LG) duration 110 frames exceeds threshold 90 frames [start=91, end=200].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (RG) duration 110 frames exceeds threshold 90 frames [start=91, end=200].
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '18' (SAF1) duration 110 frames exceeds threshold 90 frames [start=91, end=200].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (C) duration 110 frames exceeds threshold 90 frames [start=91, end=200].
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [89–104], lower_priority='Action_ZoneBlock' annotated_start=91, effective_Action_ZoneBlock_start=105.
- ⚠️ Action 'Action_None' range [89-168] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-299] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [120-233] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [235-250] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [255-256] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-118] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-140] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-151] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-199] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-259] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-186] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-194] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-216] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-179] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-208] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-191] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-262] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-270] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-189] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-114] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-227] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-204] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-212] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-235] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-260] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-273] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-280] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-290] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-190] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-219] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-256] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-200] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-268] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [91-183] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [186-187] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-169] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-181] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-188] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-217] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [105-109] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-122] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-258] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-147] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-248] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-260] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-270] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-197] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-196] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-248] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-188] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-221] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-191] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-217] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-232] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-237] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-250] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-256] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-280] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-292] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-268] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-293] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '38' has 1 frames without a visible bounding box.
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

</details>