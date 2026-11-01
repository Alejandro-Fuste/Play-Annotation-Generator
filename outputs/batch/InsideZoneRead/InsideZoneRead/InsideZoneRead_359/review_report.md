# Play-Annotation-Generator Annotation Review — InsideZoneRead_359

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_359`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 123
- **Validation Warnings:** 141
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 97
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `17` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Keep` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 16 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 17 | START | 17 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 20 | START | 31 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `15` | `14` | 20 | START | 20 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `16` | `15` | 20 | START | 20 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `17` | `16` | 20 | START | 20 | 42 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 30 | END | 17 | 30 |
| ✅ EXACT | `Action_ReadDefender` | QB | `9` | `8` | 35 | START | 35 | 42 |
| ✅ EXACT | `Action_Keep` | QB | `9` | `8` | 43 | START | 43 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `9` | `8` | 62 | START | 62 | 129 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 104 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_SnapReceive` | 17 | 30 | 14 | inferred_complete_timeline |
| `Action_None` | 31 | 34 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 35 | 42 | 8 | inferred_complete_timeline |
| `Action_Keep` | 43 | 61 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 62 | 129 | 68 | inferred_complete_timeline |
| `Action_BallCarry` | 133 | 136 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 141 | 148 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 150 | 210 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 50 | 34 | inferred_complete_timeline |
| `Action_None` | 52 | 84 | 33 | inferred_complete_timeline |
| `Action_None` | 98 | 101 | 4 | inferred_complete_timeline |
| `Action_None` | 103 | 210 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 210 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 210 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 210 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 129 | 113 | inferred_complete_timeline |
| `Action_None` | 141 | 145 | 5 | inferred_complete_timeline |
| `Action_None` | 159 | 163 | 5 | inferred_complete_timeline |
| `Action_None` | 167 | 210 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 42 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 57 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 83 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 104 | 15 | inferred_complete_timeline |
| `Action_None` | 105 | 186 | 82 | inferred_complete_timeline |
| `Action_None` | 191 | 193 | 3 | inferred_complete_timeline |
| `Action_None` | 197 | 210 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_BallSnap` | 17 | 30 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 41 | 47 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 104 | 55 | inferred_complete_timeline |
| `Action_None` | 105 | 210 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 19 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 28 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 104 | 34 | inferred_complete_timeline |
| `Action_None` | 105 | 208 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 26 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 35 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 73 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 76 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 16 | 13 | inferred_complete_timeline |
| `Action_None` | 17 | 143 | 127 | inferred_complete_timeline |
| `Action_None` | 146 | 154 | 9 | inferred_complete_timeline |
| `Action_None` | 164 | 210 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 102 | 86 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 134 | 118 | inferred_complete_timeline |
| `Action_None` | 139 | 165 | 27 | inferred_complete_timeline |
| `Action_None` | 167 | 210 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 186 | 170 | inferred_complete_timeline |
| `Action_None` | 191 | 196 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 181 | 165 | inferred_complete_timeline |
| `Action_None` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_None` | 190 | 210 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 76 | 60 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 210 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 176 | 160 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `20` | Position_Unknown | Team_Unknown | 20–98 | 31 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 21–153 | 126 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 30–39 | 10 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 31–185 | 136 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 43–127 | 70 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 96–101 | 4 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 115–136 | 22 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 123–210 | 53 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 124–210 | 61 | 6 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 130–133 | 4 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 137–206 | 32 | 5 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 146–148 | 3 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 150–210 | 51 | 6 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 151–152 | 2 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 158–210 | 53 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 159–191 | 31 | 2 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 161–210 | 50 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 163–210 | 48 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 192–210 | 19 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 195–196 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (7 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (7 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (7 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 98 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 718: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [17–30], lower_priority='Action_ZoneBlock' annotated_start=20, effective_Action_ZoneBlock_start=31.
- ⚠️ Action 'Action_None' range [17-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-186] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-196] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-210] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-50] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-84] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-181] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-176] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-102] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [62-129] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [133-136] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [141-148] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [150-210] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-76] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-129] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-145] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-163] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-165] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-32] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [41-47] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-26] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-35] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [61-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [75-76] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-28] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-32] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-208] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-42] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-57] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-83] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-186] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-143] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-154] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-210] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-39] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-45] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-98] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-140] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-39] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-35] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-56] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-167] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-45] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-77] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-116] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-136] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-167] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-134] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-151] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-169] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-165] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-175] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-160] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-167] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-182] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-201] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-174] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-191] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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