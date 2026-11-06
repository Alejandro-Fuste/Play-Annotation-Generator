# Play-Annotation-Generator Annotation Review — OutsideZoneRead_119

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_119`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 85
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LG | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `18` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `21` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_BallSnap` | LG | `20` | `19` | 16 | START | 16 | 18 |
| ✅ EXACT | `Action_ZoneBlock` | C | `13` | `12` | 19 | START | 19 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `16` | `15` | 19 | START | 19 | 42 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `17` | `16` | 19 | START | 19 | 84 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `20` | `19` | 19 | START | 19 | 84 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `22` | `21` | 19 | START | 19 | 84 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 28 | END | 16 | 28 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `10` | `9` | 34 | START | 34 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | `16` | `15` | 43 | START | 43 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | `10` | `9` | 47 | START | 47 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `10` | `9` | 70 | START | 70 | 179 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 84 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 16 | 28 | 13 | inferred_complete_timeline |
| `Action_None` | 29 | 33 | 5 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 34 | 46 | 13 | inferred_complete_timeline |
| `Action_Keep` | 47 | 63 | 17 | inferred_complete_timeline |
| `Action_Keep` | 65 | 69 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 70 | 179 | 110 | inferred_complete_timeline |
| `Action_BallCarry` | 185 | 193 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 196 | 210 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 203 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 173 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–36
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 36 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 210 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 210 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 84 | 66 | inferred_complete_timeline |
| `Action_None` | 85 | 210 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_BallSnap` | 16 | 18 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 84 | 66 | inferred_complete_timeline |
| `Action_None` | 85 | 210 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–34
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 34 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 84 | 66 | inferred_complete_timeline |
| `Action_None` | 85 | 210 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 42 | 24 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 43 | 67 | 25 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 72 | 84 | 13 | inferred_complete_timeline |
| `Action_None` | 85 | 210 | 126 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 58 | 43 | inferred_complete_timeline |
| `Action_None` | 63 | 85 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 191 | 176 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 60 | 45 | inferred_complete_timeline |
| `Action_None` | 131 | 210 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 120 | 105 | inferred_complete_timeline |
| `Action_None` | 122 | 140 | 19 | inferred_complete_timeline |
| `Action_None` | 149 | 210 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 154 | 139 | inferred_complete_timeline |
| `Action_None` | 173 | 186 | 14 | inferred_complete_timeline |
| `Action_None` | 188 | 190 | 3 | inferred_complete_timeline |
| `Action_None` | 192 | 210 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 210 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 210 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>LB4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 95 | 80 | inferred_complete_timeline |
| `Action_None` | 97 | 112 | 16 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 157 | 142 | inferred_complete_timeline |
| `Action_None` | 159 | 161 | 3 | inferred_complete_timeline |
| `Action_None` | 163 | 210 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 130 | 115 | inferred_complete_timeline |
| `Action_None` | 133 | 159 | 27 | inferred_complete_timeline |
| `Action_None` | 161 | 210 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 210 | 195 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 24–38 | 4 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 43–210 | 158 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 60–116 | 57 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 65–210 | 142 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 90–204 | 110 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 110–112 | 3 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 126–205 | 36 | 5 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 139–140 | 2 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 148–210 | 63 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 203–210 | 7 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 204–208 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 62 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [16-95] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-112] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-130] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-159] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-191] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-203] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-173] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-60] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [47-63] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [70-179] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [185-193] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [196-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-157] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-120] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-140] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-34] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-58] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [43-67] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-36] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-154] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-186] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-25] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-38] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-113] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-116] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-82] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-110] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-180] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-204] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-142] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-151] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-166] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '32' has 1 frames without a visible bounding box.
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

</details>