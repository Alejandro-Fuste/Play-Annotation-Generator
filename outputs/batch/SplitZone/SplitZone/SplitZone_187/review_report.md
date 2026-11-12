# Play-Annotation-Generator Annotation Review — SplitZone_187

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_187`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 97
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | LB2 | defense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 1 | START | 2 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 1 | START | 2 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `10` | `Group` | 1 | START | 2 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 1 | START | 2 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 1 | START | 2 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 1 | START | 2 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 1 | START | 2 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 1 | START | 2 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 1 | START | 2 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 1 | START | 2 | 121 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 92 | START | 92 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `14` | `14` | 95 | START | 95 | 157 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `18` | 95 | START | 104 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `2` | `2` | 95 | START | 95 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `20` | 95 | START | 95 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `3` | `3` | 95 | START | 95 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | LB2 | `8` | `8` | 97 | START | 97 | 152 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 103 | END | 92 | 103 |
| ✅ EXACT | `Action_Handoff` | QB | `16` | `16` | 114 | START | 114 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `4` | 122 | START | 122 | 127 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 244 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 91 | 90 | inferred_complete_timeline |
| `Action_SnapReceive` | 92 | 103 | 12 | inferred_complete_timeline |
| `Action_None` | 104 | 113 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 114 | 121 | 8 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 121 | 120 | inferred_complete_timeline |
| `Action_BallCarry` | 122 | 127 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 130 | 194 | 65 | inferred_complete_timeline |
| `Action_BallCarry` | 196 | 299 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 2–148
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 91 | 90 | inferred_complete_timeline |
| `Action_None` | 92 | 148 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 91 | 90 | inferred_complete_timeline |
| `Action_None` | 92 | 299 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 91 | 90 | inferred_complete_timeline |
| `Action_None` | 92 | 143 | 52 | inferred_complete_timeline |
| `Action_None` | 146 | 198 | 53 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |
| `Action_None` | 213 | 238 | 26 | inferred_complete_timeline |
| `Action_None` | 248 | 299 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 2–160
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 94 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 157 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 159 | 160 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 94 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 145 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 170 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 244 | 62 | inferred_complete_timeline |
| `Action_None` | 245 | 299 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 91 | 90 | inferred_complete_timeline |
| `Action_BallSnap` | 92 | 103 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 109 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 113 | 115 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 141 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 150 | 169 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 177 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 179 | 244 | 66 | inferred_complete_timeline |
| `Action_None` | 245 | 270 | 26 | inferred_complete_timeline |
| `Action_None` | 275 | 299 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 2–155
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 94 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 144 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 155 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 94 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 156 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 158 | 161 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 197 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 200 | 244 | 45 | inferred_complete_timeline |
| `Action_None` | 245 | 252 | 8 | inferred_complete_timeline |
| `Action_None` | 255 | 299 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 91 | 90 | inferred_complete_timeline |
| `Action_None` | 92 | 116 | 25 | inferred_complete_timeline |
| `Action_None` | 130 | 147 | 18 | inferred_complete_timeline |
| `Action_None` | 153 | 157 | 5 | inferred_complete_timeline |
| `Action_None` | 163 | 168 | 6 | inferred_complete_timeline |
| `Action_None` | 170 | 185 | 16 | inferred_complete_timeline |
| `Action_None` | 188 | 299 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `24`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `24`
- **team_side:** `defense`
- **Visible Frames:** 13–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 16 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 91 | 69 | inferred_complete_timeline |
| `Action_None` | 92 | 98 | 7 | inferred_complete_timeline |
| `Action_None` | 102 | 299 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 91 | 90 | inferred_complete_timeline |
| `Action_None` | 92 | 148 | 57 | inferred_complete_timeline |
| `Action_None` | 150 | 260 | 111 | inferred_complete_timeline |
| `Action_None` | 266 | 299 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 91 | 90 | inferred_complete_timeline |
| `Action_None` | 92 | 164 | 73 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_None` | 176 | 188 | 13 | inferred_complete_timeline |
| `Action_None` | 191 | 204 | 14 | inferred_complete_timeline |
| `Action_None` | 211 | 282 | 72 | inferred_complete_timeline |
| `Action_None` | 284 | 299 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 91 | 90 | inferred_complete_timeline |
| `Action_None` | 92 | 157 | 66 | inferred_complete_timeline |
| `Action_None` | 159 | 299 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 96 | 95 | inferred_complete_timeline |
| `Action_SplitBlock` | 97 | 152 | 56 | inferred_complete_timeline |
| `Action_SplitBlock` | 154 | 244 | 91 | inferred_complete_timeline |
| `Action_None` | 245 | 299 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 91 | 90 | inferred_complete_timeline |
| `Action_None` | 92 | 299 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 91 | 90 | inferred_complete_timeline |
| `Action_None` | 92 | 242 | 151 | inferred_complete_timeline |
| `Action_None` | 245 | 299 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 91 | 90 | inferred_complete_timeline |
| `Action_None` | 92 | 299 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 91 | 90 | inferred_complete_timeline |
| `Action_None` | 92 | 202 | 111 | inferred_complete_timeline |
| `Action_None` | 204 | 299 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 91 | 90 | inferred_complete_timeline |
| `Action_None` | 92 | 299 | 208 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 2–193 | 180 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 53–88 | 11 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 88–111 | 24 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 120–121 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 149–150 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 180–292 | 106 | 5 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 189–191 | 3 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 219–299 | 81 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 224–236 | 12 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 230–299 | 70 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 249–252 | 4 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 251–252 | 2 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 254–255 | 2 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 269–299 | 31 | 1 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (5 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 376: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (LG) duration 150 frames exceeds threshold 90 frames [start=95, end=244].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (RT) duration 150 frames exceeds threshold 90 frames [start=95, end=244].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (C) duration 150 frames exceeds threshold 90 frames [start=95, end=244].
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [92–103], lower_priority='Action_ZoneBlock' annotated_start=95, effective_Action_ZoneBlock_start=104.
- ⚠️ Action 'Action_None' range [92-148] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-145] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [147-170] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [179-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [183-244] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-156] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [158-161] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [188-189] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-197] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-252] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [122-127] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [130-194] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-193] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [97-152] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-143] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-198] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-238] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-202] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-116] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-157] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-185] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-242] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-299] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-157] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [159-160] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-148] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-260] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-109] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [113-115] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [137-141] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [150-169] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [173-177] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [179-244] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-270] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-164] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-188] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-204] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-282] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-144] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [154-155] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-16] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-91] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-98] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-55] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-66] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-88] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-245] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-251] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-263] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-288] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-299] for track '28' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-233] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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

</details>