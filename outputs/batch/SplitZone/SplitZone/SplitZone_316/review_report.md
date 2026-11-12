# Play-Annotation-Generator Annotation Review — SplitZone_316

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_316`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 10
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | WR1 | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `20` | `20` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `6` | `6` |
| ✅ EXACT | `Action_PressEdge` | DE1 | defense | `14` | `14` |
| ✅ EXACT | `Action_Handoff` | DE1 | defense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE1 | defense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `0` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 66 |
| ✅ EXACT | `Action_BallSnap` | WR1 | `11` | `11` | 53 | START | 53 | 65 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `0` | `0` | 63 | START | 63 | 109 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `1` | `1` | 63 | START | 63 | 109 |
| ✅ EXACT | `Action_ZoneBlock` | C | `18` | `18` | 63 | START | 63 | 109 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `2` | 63 | START | 63 | 109 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `4` | `4` | 63 | START | 63 | 109 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `20` | `20` | 65 | END | 53 | 65 |
| ✅ EXACT | `Action_SplitBlock` | TE | `6` | `6` | 67 | START | 67 | 113 |
| ✅ EXACT | `Action_PressEdge` | DE1 | `14` | `14` | 71 | START | 71 | 85 |
| ✅ EXACT | `Action_Handoff` | DE1 | `14` | `14` | 86 | START | 86 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE1 | `14` | `14` | 98 | START | 98 | 253 |

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
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 269 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 269 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_BallSnap` | 53 | 65 | 13 | inferred_complete_timeline |
| `Action_None` | 66 | 155 | 90 | inferred_complete_timeline |
| `Action_None` | 158 | 167 | 10 | inferred_complete_timeline |
| `Action_None` | 176 | 269 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 141 | 89 | inferred_complete_timeline |
| `Action_None` | 144 | 163 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_SplitBlock` | 67 | 113 | 47 | inferred_complete_timeline |
| `Action_None` | 114 | 269 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 109 | 47 | inferred_complete_timeline |
| `Action_None` | 110 | 158 | 49 | inferred_complete_timeline |
| `Action_None` | 161 | 192 | 32 | inferred_complete_timeline |
| `Action_None` | 195 | 269 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 109 | 47 | inferred_complete_timeline |
| `Action_None` | 110 | 269 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 109 | 47 | inferred_complete_timeline |
| `Action_None` | 110 | 192 | 83 | inferred_complete_timeline |
| `Action_None` | 194 | 264 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 109 | 47 | inferred_complete_timeline |
| `Action_None` | 110 | 269 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 109 | 47 | inferred_complete_timeline |
| `Action_None` | 110 | 140 | 31 | inferred_complete_timeline |
| `Action_None` | 146 | 152 | 7 | inferred_complete_timeline |
| `Action_None` | 154 | 158 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_PressEdge` | 71 | 85 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 86 | 97 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 98 | 253 | 156 | inferred_complete_timeline |
| `Action_BallCarry` | 258 | 269 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 269 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 269 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 192 | 140 | inferred_complete_timeline |
| `Action_None` | 195 | 269 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 269 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 269 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 267 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 98 | 46 | inferred_complete_timeline |
| `Action_None` | 101 | 269 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 88 | 36 | inferred_complete_timeline |
| `Action_None` | 90 | 92 | 3 | inferred_complete_timeline |
| `Action_None` | 94 | 269 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 77 | 25 | inferred_complete_timeline |
| `Action_None` | 83 | 104 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–269 | 270 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–269 | 270 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 96–98 | 3 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 103–104 | 2 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 130–166 | 30 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 176–269 | 94 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 177–269 | 92 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 177–266 | 90 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 198–258 | 16 | 5 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 206–249 | 39 | 3 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 207–247 | 35 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 209–238 | 20 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 217–220 | 4 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 217–268 | 44 | 6 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 222–226 | 5 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 222–224 | 3 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 240–268 | 10 | 3 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 245–269 | 13 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `SAF2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 58 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [110-158] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-192] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-141] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-163] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-140] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-152] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-158] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-269] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-98] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-269] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-192] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-155] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-167] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-267] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [98-253] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [258-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-77] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-104] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-192] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-264] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-88] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-92] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-98] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-138] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-163] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-264] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-266] for track '27' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-214] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-249] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-217] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-247] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-238] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-220] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-229] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-242] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-254] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-262] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-226] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-253] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-257] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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