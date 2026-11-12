# Play-Annotation-Generator Annotation Review — SplitZone_171

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_171`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 96
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `2` | `2` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `6` | `6` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `10` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 17 | START | 18 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 17 | START | 18 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 17 | START | 18 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 17 | START | 18 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 17 | START | 18 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 17 | START | 18 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 17 | START | 18 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 17 | START | 18 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 17 | START | 18 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 17 | START | 18 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `9` | `Group` | 17 | START | 18 | 95 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 89 | START | 89 | 101 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `13` | `13` | 92 | START | 92 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `18` | 92 | START | 92 | 109 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `2` | `2` | 92 | START | 92 | 153 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `20` | `20` | 92 | START | 102 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `6` | `6` | 92 | START | 92 | 137 |
| ✅ EXACT | `Action_SplitBlock` | HB | `9` | `9` | 96 | START | 96 | 166 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 101 | END | 89 | 101 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `19` | 107 | START | 107 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `10` | `10` | 114 | START | 114 | 117 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 166 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 18–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 88 | 71 | inferred_complete_timeline |
| `Action_SnapReceive` | 89 | 101 | 13 | inferred_complete_timeline |
| `Action_None` | 102 | 106 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 107 | 113 | 7 | inferred_complete_timeline |
| `Action_None` | 114 | 269 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 18–268
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 113 | 96 | inferred_complete_timeline |
| `Action_BallCarry` | 114 | 117 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 120 | 268 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 18–269
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 95 | 78 | inferred_complete_timeline |
| `Action_SplitBlock` | 96 | 166 | 71 | inferred_complete_timeline |
| `Action_None` | 167 | 183 | 17 | inferred_complete_timeline |
| `Action_None` | 188 | 192 | 5 | inferred_complete_timeline |
| `Action_None` | 194 | 269 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 18–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 88 | 71 | inferred_complete_timeline |
| `Action_None` | 89 | 269 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 18–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 88 | 71 | inferred_complete_timeline |
| `Action_None` | 89 | 269 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 18–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 88 | 71 | inferred_complete_timeline |
| `Action_None` | 89 | 115 | 27 | inferred_complete_timeline |
| `Action_None` | 117 | 269 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 18–232
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 91 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 166 | 75 | inferred_complete_timeline |
| `Action_None` | 167 | 188 | 22 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_None` | 194 | 228 | 35 | inferred_complete_timeline |
| `Action_None` | 230 | 232 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 18–269
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 91 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 153 | 62 | inferred_complete_timeline |
| `Action_None` | 175 | 232 | 58 | inferred_complete_timeline |
| `Action_None` | 237 | 238 | 2 | inferred_complete_timeline |
| `Action_None` | 245 | 269 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 18–269
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 88 | 71 | inferred_complete_timeline |
| `Action_BallSnap` | 89 | 101 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 166 | 65 | inferred_complete_timeline |
| `Action_None` | 167 | 197 | 31 | inferred_complete_timeline |
| `Action_None` | 200 | 203 | 4 | inferred_complete_timeline |
| `Action_None` | 207 | 217 | 11 | inferred_complete_timeline |
| `Action_None` | 219 | 269 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 18–269
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 91 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 109 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 166 | 44 | inferred_complete_timeline |
| `Action_None` | 167 | 269 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 18–269
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 91 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 137 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 140 | 166 | 27 | inferred_complete_timeline |
| `Action_None` | 167 | 269 | 103 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 18–179
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 88 | 71 | inferred_complete_timeline |
| `Action_None` | 89 | 164 | 76 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 18–139
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 88 | 71 | inferred_complete_timeline |
| `Action_None` | 89 | 139 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 18–172
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 88 | 71 | inferred_complete_timeline |
| `Action_None` | 89 | 107 | 19 | inferred_complete_timeline |
| `Action_None` | 110 | 114 | 5 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_None` | 130 | 135 | 6 | inferred_complete_timeline |
| `Action_None` | 142 | 146 | 5 | inferred_complete_timeline |
| `Action_None` | 148 | 150 | 3 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 18–269
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 88 | 71 | inferred_complete_timeline |
| `Action_None` | 89 | 122 | 34 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 144 | 146 | 3 | inferred_complete_timeline |
| `Action_None` | 148 | 150 | 3 | inferred_complete_timeline |
| `Action_None` | 155 | 269 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 18–269
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 88 | 71 | inferred_complete_timeline |
| `Action_None` | 89 | 148 | 60 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 157 | 160 | 4 | inferred_complete_timeline |
| `Action_None` | 180 | 269 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 18–136
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 88 | 71 | inferred_complete_timeline |
| `Action_None` | 89 | 136 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 18–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 88 | 71 | inferred_complete_timeline |
| `Action_None` | 89 | 269 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 18–175
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 88 | 71 | inferred_complete_timeline |
| `Action_None` | 89 | 128 | 40 | inferred_complete_timeline |
| `Action_None` | 141 | 155 | 15 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 18–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 88 | 71 | inferred_complete_timeline |
| `Action_None` | 89 | 269 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 18–269
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 88 | 71 | inferred_complete_timeline |
| `Action_None` | 89 | 139 | 51 | inferred_complete_timeline |
| `Action_None` | 144 | 165 | 22 | inferred_complete_timeline |
| `Action_None` | 167 | 173 | 7 | inferred_complete_timeline |
| `Action_None` | 178 | 180 | 3 | inferred_complete_timeline |
| `Action_None` | 182 | 186 | 5 | inferred_complete_timeline |
| `Action_None` | 188 | 192 | 5 | inferred_complete_timeline |
| `Action_None` | 194 | 269 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 18–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 88 | 71 | inferred_complete_timeline |
| `Action_None` | 89 | 150 | 62 | inferred_complete_timeline |
| `Action_None` | 152 | 269 | 118 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `28` | Position_Unknown | Team_Unknown | 156–269 | 113 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 161–217 | 45 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 183–269 | 87 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 195–269 | 75 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 195–222 | 16 | 3 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 202–269 | 68 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 211–243 | 25 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 215–216 | 2 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 215–242 | 19 | 4 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 229–264 | 20 | 4 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 234–247 | 12 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 235–269 | 35 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 264–266 | 3 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 267–269 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `20` (C): Annotated start 92 != Inferred start 102
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [89–101], lower_priority='Action_ZoneBlock' annotated_start=92, effective_Action_ZoneBlock_start=102.
- ⚠️ Action 'Action_ZoneBlock' range [92-153] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-232] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-139] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-115] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-136] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-137] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-122] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-269] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-183] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-192] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [114-117] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [120-268] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-269] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-166] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-188] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-228] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-165] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-186] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-192] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-269] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-164] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-114] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-135] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-109] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-166] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-197] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-217] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-148] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-228] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-173] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-217] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-212] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-222] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-243] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-228] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-242] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-254] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-247] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '34' has 1 frames without a visible bounding box.
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