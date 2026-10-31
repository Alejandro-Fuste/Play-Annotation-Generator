# Play-Annotation-Generator Annotation Review — Hitch_72

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Hitch_72`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_Hitch`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 159
- **Validation Warnings:** 180
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 138
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_RunHitchRoute` | WR3 | offense | `6` | `6` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `44` | `30` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 40 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 26 | START | 26 | 28 |
| ✅ EXACT | `Action_PassBlock` | LT | `15` | `15` | 28 | START | 28 | 90 |
| ✅ EXACT | `Action_PassBlock` | RT | `16` | `16` | 28 | START | 28 | 269 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `17` | `17` | 28 | START | 28 | 153 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 28 | START | 39 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 28 | START | 28 | 33 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 38 | END | 26 | 38 |
| ✅ EXACT | `Action_RunHitchRoute` | WR3 | `6` | `6` | 41 | START | 41 | 153 |
| ✅ EXACT | `Action_ThrowPass` | QB | `18` | `18` | 108 | START | 108 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `44` | `30` | 154 | START | 158 | 210 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_SnapReceive` | 26 | 38 | 13 | inferred_complete_timeline |
| `Action_None` | 39 | 69 | 31 | inferred_complete_timeline |
| `Action_None` | 71 | 107 | 37 | inferred_complete_timeline |
| `Action_ThrowPass` | 108 | 118 | 11 | inferred_complete_timeline |
| `Action_None` | 119 | 152 | 34 | inferred_complete_timeline |
| `Action_None` | 157 | 162 | 6 | inferred_complete_timeline |
| `Action_None` | 173 | 176 | 4 | inferred_complete_timeline |
| `Action_None` | 179 | 184 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 78 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 41 | 153 | 113 | inferred_complete_timeline |
| `Action_None` | 154 | 187 | 34 | inferred_complete_timeline |
| `Action_None` | 189 | 198 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 237 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 27 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 90 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 153 | 126 | inferred_complete_timeline |
| `Action_PassBlock` | 159 | 162 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 165 | 167 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 173 | 175 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 203 | 227 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 235 | 269 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_BallSnap` | 26 | 28 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 49 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 269 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–38
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 27 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 33 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 38 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 269 | 242 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–43
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 43 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 87 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–246
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 118 | 93 | inferred_complete_timeline |
| `Action_None` | 127 | 132 | 6 | inferred_complete_timeline |
| `Action_None` | 142 | 160 | 19 | inferred_complete_timeline |
| `Action_None` | 162 | 168 | 7 | inferred_complete_timeline |
| `Action_None` | 172 | 175 | 4 | inferred_complete_timeline |
| `Action_None` | 184 | 187 | 4 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |
| `Action_None` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_None` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_None` | 215 | 220 | 6 | inferred_complete_timeline |
| `Action_None` | 238 | 240 | 3 | inferred_complete_timeline |
| `Action_None` | 245 | 246 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 123 | 98 | inferred_complete_timeline |
| `Action_None` | 126 | 132 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 269 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 94 | 69 | inferred_complete_timeline |
| `Action_None` | 100 | 127 | 28 | inferred_complete_timeline |
| `Action_None` | 132 | 240 | 109 | inferred_complete_timeline |
| `Action_None` | 242 | 269 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 59 | 34 | inferred_complete_timeline |
| `Action_None` | 61 | 63 | 3 | inferred_complete_timeline |
| `Action_None` | 74 | 76 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 90 | 65 | inferred_complete_timeline |
| `Action_None` | 95 | 138 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 89 | 64 | inferred_complete_timeline |
| `Action_None` | 91 | 94 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 108 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 269 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–242
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 238 | 213 | inferred_complete_timeline |
| `Action_None` | 240 | 242 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–44 | 45 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 41–44 | 4 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 62–269 | 168 | 4 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 75–269 | 122 | 13 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 93–269 | 101 | 12 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 102–213 | 109 | 2 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 126–269 | 129 | 5 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 131–227 | 97 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 139–269 | 111 | 3 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 140–269 | 125 | 3 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 142–269 | 121 | 5 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 147–151 | 4 | 2 | Undefined position; Undefined team |
| `33` | `52` | Position_Unknown | Team_Unknown | 157–269 | 112 | 2 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 158–177 | 16 | 2 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 190–191 | 2 | 1 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 191–201 | 6 | 2 | Undefined position; Undefined team |
| `37` | `57` | Position_Unknown | Team_Unknown | 195–200 | 6 | 1 | Undefined position; Undefined team |
| `38` | `58` | Position_Unknown | Team_Unknown | 195–213 | 18 | 2 | Undefined position; Undefined team |
| `39` | `60` | Position_Unknown | Team_Unknown | 223–240 | 11 | 2 | Undefined position; Undefined team |
| `40` | `62` | Position_Unknown | Team_Unknown | 231–269 | 28 | 4 | Undefined position; Undefined team |
| `41` | `63` | Position_Unknown | Team_Unknown | 244–247 | 4 | 1 | Undefined position; Undefined team |
| `42` | `65` | Position_Unknown | Team_Unknown | 254–269 | 16 | 1 | Undefined position; Undefined team |
| `43` | `67` | Position_Unknown | Team_Unknown | 256–269 | 14 | 1 | Undefined position; Undefined team |
| `44` | `68` | Position_Unknown | Team_Unknown | 258–268 | 8 | 2 | Undefined position; Undefined team |
| `45` | `69` | Position_Unknown | Team_Unknown | 258–269 | 10 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `30` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 126 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 81: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ Row 82: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [26–38], lower_priority='Action_PassBlock' annotated_start=28, effective_Action_PassBlock_start=39.
- ⚠️ Action 'Action_None' range [26-237] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-94] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-127] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-240] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-78] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-108] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-87] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-90] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-187] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-198] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-89] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-238] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-59] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-63] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-76] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-123] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-132] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-118] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-132] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-160] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-168] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-220] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-43] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-90] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-153] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [159-162] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [165-167] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [173-175] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [194-195] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [203-227] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-69] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-107] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-152] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-162] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-184] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-44] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [26-28] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-40] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-49] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-269] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-33] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-38] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-44] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-114] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-198] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-217] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-269] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-112] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-129] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-183] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-201] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-266] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-111] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-137] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-178] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-191] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-235] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-260] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-200] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-213] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-227] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-247] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-227] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-150] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-248] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-153] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [158-210] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [212-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-191] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-221] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-161] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-269] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-177] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-200] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-209] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-229] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-240] for track '40' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-269] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '45' has 1 frames without a visible bounding box.
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

</details>