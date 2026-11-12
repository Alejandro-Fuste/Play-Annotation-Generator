# Play-Annotation-Generator Annotation Review — SplitZone_307

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_307`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 81
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
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DE1 | defense | `15` | `15` |
| ✅ EXACT | `Action_SplitBlock` | SAF1 | defense | `7` | `7` |
| ✅ EXACT | `Action_PressEdge` | CB2 | defense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | LB3 | defense | `11` | `11` |
| ✅ EXACT | `Action_ReadEdgeDefender` | LB3 | defense | `11` | `11` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `24` | `23` |
| ✅ EXACT | `Action_Handoff` | LB3 | defense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `12` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 3 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `20` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `3` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 60 |
| ✅ EXACT | `Action_BallSnap` | DE1 | `15` | `15` | 63 | START | 63 | 75 |
| ✅ EXACT | `Action_SplitBlock` | SAF1 | `7` | `7` | 72 | START | 72 | 92 |
| ✅ EXACT | `Action_PressEdge` | CB2 | `16` | `16` | 73 | START | 73 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `17` | 73 | START | 73 | 85 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `20` | `20` | 73 | START | 73 | 107 |
| ✅ EXACT | `Action_ZoneBlock` | C | `3` | `3` | 73 | START | 73 | 107 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `8` | 73 | START | 73 | 107 |
| ✅ EXACT | `Action_SnapReceive` | LB3 | `11` | `11` | 75 | END | 63 | 75 |
| ✅ EXACT | `Action_ReadEdgeDefender` | LB3 | `11` | `11` | 77 | START | 77 | 94 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `24` | `23` | 107 | START | 107 | 265 |
| ✅ EXACT | `Action_Handoff` | LB3 | `11` | `11` | 107 | START | 107 | 158 |

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
- **Visible Frames:** 3–5
- **Visible Samples:** 3

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 5 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 130 | 68 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 101 | 39 | inferred_complete_timeline |
| `Action_None` | 105 | 107 | 3 | inferred_complete_timeline |
| `Action_None` | 113 | 141 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 121 | 59 | inferred_complete_timeline |
| `Action_None` | 127 | 135 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 269 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 140 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 85 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 107 | 17 | inferred_complete_timeline |
| `Action_None` | 108 | 122 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 107 | 35 | inferred_complete_timeline |
| `Action_None` | 108 | 138 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 73–127
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 73 | 107 | 35 | inferred_complete_timeline |
| `Action_None` | 108 | 127 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 72 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 107 | 35 | inferred_complete_timeline |
| `Action_None` | 108 | 110 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_BallSnap` | 63 | 75 | 13 | inferred_complete_timeline |
| `Action_None` | 76 | 91 | 16 | inferred_complete_timeline |
| `Action_None` | 95 | 146 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 233 | 171 | inferred_complete_timeline |
| `Action_None` | 235 | 269 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 73 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 152 | 90 | inferred_complete_timeline |
| `Action_None` | 155 | 158 | 4 | inferred_complete_timeline |
| `Action_None` | 161 | 165 | 5 | inferred_complete_timeline |
| `Action_None` | 169 | 206 | 38 | inferred_complete_timeline |
| `Action_None` | 211 | 214 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 259 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_SnapReceive` | 63 | 75 | 13 | inferred_complete_timeline |
| `Action_None` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 77 | 94 | 18 | inferred_complete_timeline |
| `Action_None` | 95 | 106 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 107 | 158 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 144 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PressEdge` | 73 | 97 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 72 | 10 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_None` | 101 | 119 | 19 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 71 | 1 | inferred_complete_timeline |
| `Action_SplitBlock` | 72 | 92 | 21 | inferred_complete_timeline |
| `Action_None` | 93 | 269 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 99 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 94–269 | 169 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 101–269 | 169 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 106–265 | 160 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 112–155 | 44 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 117–149 | 33 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 137–156 | 6 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 153–167 | 12 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 156–269 | 111 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 157–193 | 37 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 211–231 | 21 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 229–247 | 10 | 3 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 230–269 | 40 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 55 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '21' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-233] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-73] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-138] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-140] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-121] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-259] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-269] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-99] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-152] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-206] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [107-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-101] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-130] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-144] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-91] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-146] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [73-97] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-85] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-89] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-122] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-72] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-119] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-5] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-127] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-176] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [107-265] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-155] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-149] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-167] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-235] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-193] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-231] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-242] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-269] for track '32' has 2 frames without a visible bounding box.
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

</details>