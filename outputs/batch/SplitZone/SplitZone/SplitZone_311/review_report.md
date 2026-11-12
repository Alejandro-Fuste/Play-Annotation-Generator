# Play-Annotation-Generator Annotation Review — SplitZone_311

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_311`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 103
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT1 | defense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ✅ EXACT | `Action_SplitBlock` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | CB1 | defense | `13` | `13` |
| ❌ MISSING SEGMENT | `Action_Handoff` | CB1 | defense | `13` | `13` |
| ✅ EXACT | `Action_PressEdge` | CB1 | defense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE1 | defense | `14` | `14` |
| ✅ EXACT | `Action_BlockSecondLevel` | DT2 | defense | `18` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `19` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `20` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `21` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 64 |
| ✅ EXACT | `Action_BallSnap` | DT1 | `16` | `16` | 55 | START | 55 | 67 |
| ✅ EXACT | `Action_ZoneBlock` | C | `12` | `12` | 64 | START | 64 | 105 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `15` | `15` | 64 | START | 64 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `18` | 64 | START | 71 | 75 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LT | `20` | `19` | 64 | START | 80 | 81 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `5` | 64 | START | 64 | 86 |
| ✅ EXACT | `Action_SplitBlock` | QB | `8` | `8` | 65 | START | 65 | 67 |
| ✅ EXACT | `Action_SnapReceive` | CB1 | `13` | `13` | 69 | END | 55 | 69 |
| ❌ MISSING SEGMENT | `Action_Handoff` | CB1 | `13` | `13` | 87 | START | N/A | N/A |
| ✅ EXACT | `Action_PressEdge` | CB1 | `13` | `13` | 87 | START | 87 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE1 | `14` | `14` | 100 | START | 100 | 156 |
| ✅ EXACT | `Action_BlockSecondLevel` | DT2 | `18` | `17` | 125 | START | 125 | 137 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_SplitBlock` | 65 | 67 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 97 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–296
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 55 | 1 | inferred_complete_timeline |
| `Action_None` | 59 | 287 | 229 | inferred_complete_timeline |
| `Action_None` | 295 | 296 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 54 | 39 | inferred_complete_timeline |
| `Action_None` | 55 | 299 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 111 | 57 | inferred_complete_timeline |
| `Action_None` | 113 | 116 | 4 | inferred_complete_timeline |
| `Action_None` | 120 | 142 | 23 | inferred_complete_timeline |
| `Action_None` | 156 | 210 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 84–202
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 84 | 91 | 8 | inferred_complete_timeline |
| `Action_None` | 122 | 164 | 43 | inferred_complete_timeline |
| `Action_None` | 192 | 202 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 80–81
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 80 | 81 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 71–75
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 71 | 75 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 105 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 114 | 51 | inferred_complete_timeline |
| `Action_None` | 115 | 120 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 86 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 99 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 100 | 156 | 57 | inferred_complete_timeline |
| `Action_BallCarry` | 162 | 239 | 78 | inferred_complete_timeline |
| `Action_BallCarry` | 241 | 266 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 192 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_BallSnap` | 55 | 67 | 13 | inferred_complete_timeline |
| `Action_None` | 72 | 74 | 3 | inferred_complete_timeline |
| `Action_None` | 84 | 128 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 64–241
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 64 | 124 | 61 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 125 | 137 | 13 | inferred_complete_timeline |
| `Action_None` | 138 | 143 | 6 | inferred_complete_timeline |
| `Action_None` | 145 | 200 | 56 | inferred_complete_timeline |
| `Action_None` | 208 | 217 | 10 | inferred_complete_timeline |
| `Action_None` | 225 | 241 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 54 | 17 | inferred_complete_timeline |
| `Action_None` | 55 | 166 | 112 | inferred_complete_timeline |
| `Action_None` | 179 | 181 | 3 | inferred_complete_timeline |
| `Action_None` | 183 | 185 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 132 | 78 | inferred_complete_timeline |
| `Action_None` | 137 | 299 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–270
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_SnapReceive` | 55 | 69 | 15 | inferred_complete_timeline |
| `Action_None` | 70 | 86 | 17 | inferred_complete_timeline |
| `Action_PressEdge` | 87 | 114 | 28 | inferred_complete_timeline |
| `Action_None` | 115 | 270 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 166 | 112 | inferred_complete_timeline |
| `Action_None` | 170 | 173 | 4 | inferred_complete_timeline |
| `Action_None` | 177 | 205 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 208 | 154 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_None` | 223 | 225 | 3 | inferred_complete_timeline |
| `Action_None` | 230 | 233 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 54 | 22 | inferred_complete_timeline |
| `Action_None` | 55 | 149 | 95 | inferred_complete_timeline |
| `Action_None` | 151 | 206 | 56 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 212 | 299 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 91–92 | 2 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 101–299 | 199 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 110–299 | 165 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 124–245 | 118 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 149–299 | 129 | 7 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 162–299 | 134 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 184–299 | 116 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 190–299 | 110 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 196–231 | 12 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 197–299 | 103 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 198–299 | 102 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 219–242 | 8 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 243–299 | 57 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 271–299 | 29 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 277–299 | 23 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `20` (LT): Annotated start 64 != Inferred start 80
- ❌ Missing segment for action `Action_Handoff` on target `13` (CB1)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Overlapping action conflict at frame 87 for track '13': 'Action_Handoff' vs 'Action_PressEdge'. Overriding with 'Action_PressEdge'.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '1' starts at frame 55, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [55-55] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-287] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-166] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-205] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-111] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-142] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-208] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-86] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-149] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-206] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [65-67] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-192] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-54] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-166] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-132] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-105] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-86] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-270] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [100-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [162-239] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [241-266] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-114] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [55-67] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-74] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-128] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-143] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-200] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-217] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-241] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-75] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-81] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-91] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-164] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-202] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-139] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-164] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-245] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-190] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-214] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-223] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-263] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-184] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-203] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-231] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-224] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '32' has 1 frames without a visible bounding box.
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

</details>