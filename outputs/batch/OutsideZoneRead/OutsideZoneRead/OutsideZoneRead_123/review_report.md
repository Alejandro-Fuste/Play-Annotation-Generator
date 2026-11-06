# Play-Annotation-Generator Annotation Review — OutsideZoneRead_123

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_123`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 113
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `15` | `14` |
| ⚠️ START CHANGED | `Action_Keep` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 2 | START | 2 | 8 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `17` | 5 | START | 39 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `18` | 5 | START | 5 | 23 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 5 | START | 5 | 8 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `22` | `21` | 5 | START | 5 | 64 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 14 | END | 2 | 14 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `15` | `14` | 19 | START | 19 | 21 |
| ⚠️ START CHANGED | `Action_Keep` | QB | `15` | `14` | 23 | START | 27 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `15` | `14` | 43 | START | 43 | 67 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 64 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 2 | 14 | 13 | inferred_complete_timeline |
| `Action_None` | 15 | 16 | 2 | inferred_complete_timeline |
| `Action_None` | 18 | 18 | 1 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 19 | 21 | 3 | inferred_complete_timeline |
| `Action_Keep` | 27 | 42 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 43 | 67 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 69 | 197 | 129 | inferred_complete_timeline |
| `Action_BallCarry` | 199 | 221 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 74 | 73 | inferred_complete_timeline |
| `Action_None` | 77 | 239 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 221 | 220 | inferred_complete_timeline |
| `Action_None` | 224 | 237 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 239 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 83 | 82 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_None` | 97 | 102 | 6 | inferred_complete_timeline |
| `Action_None` | 104 | 144 | 41 | inferred_complete_timeline |
| `Action_None` | 147 | 151 | 5 | inferred_complete_timeline |
| `Action_None` | 153 | 159 | 7 | inferred_complete_timeline |
| `Action_None` | 171 | 174 | 4 | inferred_complete_timeline |
| `Action_None` | 179 | 239 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 236 | 235 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 54 | 53 | inferred_complete_timeline |
| `Action_None` | 58 | 67 | 10 | inferred_complete_timeline |
| `Action_None` | 69 | 149 | 81 | inferred_complete_timeline |
| `Action_None` | 151 | 157 | 7 | inferred_complete_timeline |
| `Action_None` | 160 | 185 | 26 | inferred_complete_timeline |
| `Action_None` | 187 | 239 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 5 | 64 | 60 | inferred_complete_timeline |
| `Action_None` | 65 | 101 | 37 | inferred_complete_timeline |
| `Action_None` | 105 | 229 | 125 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–34
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 12 | 24 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 33 | 34 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 2 | 8 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 43 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 64 | 16 | inferred_complete_timeline |
| `Action_None` | 65 | 66 | 2 | inferred_complete_timeline |
| `Action_None` | 69 | 239 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 5 | 23 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 34 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 37 | 64 | 28 | inferred_complete_timeline |
| `Action_None` | 65 | 112 | 48 | inferred_complete_timeline |
| `Action_None` | 117 | 155 | 39 | inferred_complete_timeline |
| `Action_None` | 157 | 168 | 12 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 180 | 239 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 13 | 12 | inferred_complete_timeline |
| `Action_None` | 19 | 20 | 2 | inferred_complete_timeline |
| `Action_None` | 26 | 143 | 118 | inferred_complete_timeline |
| `Action_None` | 147 | 239 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 12 | 11 | inferred_complete_timeline |
| `Action_None` | 15 | 239 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–43
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 43 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 145 | 144 | inferred_complete_timeline |
| `Action_None` | 147 | 239 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 83 | 82 | inferred_complete_timeline |
| `Action_None` | 87 | 239 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 67 | 66 | inferred_complete_timeline |
| `Action_None` | 69 | 96 | 28 | inferred_complete_timeline |
| `Action_None` | 101 | 239 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 75 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 227 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 89 | 88 | inferred_complete_timeline |
| `Action_None` | 97 | 239 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 239 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 193 | 192 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 47–50 | 4 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 53–56 | 4 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 57–96 | 8 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 69–159 | 9 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 70–239 | 170 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 70–164 | 18 | 7 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 72–239 | 168 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 84–86 | 3 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 88–140 | 52 | 2 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 97–129 | 5 | 2 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 174–239 | 66 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 186–187 | 2 | 1 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 212–239 | 28 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 217–218 | 2 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 217–221 | 4 | 2 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ `Action_Keep` for actor_track_id `15` (QB): Annotated start 23 != Inferred start 27
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [2–14], lower_priority='Action_ZoneBlock' annotated_start=5, effective_Action_ZoneBlock_start=15.
- ⚠️ Action 'Action_None' range [2-83] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-102] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-144] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-159] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-236] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-89] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-83] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-239] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-67] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-96] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-239] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-12] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-221] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-237] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-227] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-193] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-145] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-74] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-54] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-149] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-157] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-185] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-16] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadEdgeDefender' for track '14' starts at frame 19, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ReadEdgeDefender' range [19-21] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [43-67] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [69-197] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [199-221] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-75] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-13] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-20] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [2-8] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [39-43] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [5-23] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [32-34] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-112] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-155] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-168] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-43] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [5-8] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [12-24] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [33-34] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-101] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-229] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-50] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-56] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-65] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-159] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-72] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-78] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-86] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-126] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-140] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-239] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '36' has 1 frames without a visible bounding box.
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

</details>