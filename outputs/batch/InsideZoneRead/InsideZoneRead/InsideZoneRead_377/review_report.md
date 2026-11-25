# Play-Annotation-Generator Annotation Review — InsideZoneRead_377

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_377`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 71
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 9
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB1 | defense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | LB1 | defense | `9` | `8` |
| ✅ EXACT | `Action_ReadDefender` | LB1 | defense | `9` | `8` |
| ✅ EXACT | `Action_BlockSecondLevel` | WR3 | offense | `5` | `4` |
| ✅ EXACT | `Action_Keep` | LB1 | defense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB1 | defense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 44 |
| ✅ EXACT | `Action_BallSnap` | CB1 | `2` | `1` | 21 | START | 21 | 35 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `14` | `13` | 24 | START | 24 | 81 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `16` | `15` | 24 | START | 24 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `18` | `17` | 24 | START | 24 | 44 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `20` | `19` | 24 | START | 24 | 81 |
| ✅ EXACT | `Action_ZoneBlock` | C | `22` | `21` | 24 | START | 24 | 46 |
| ✅ EXACT | `Action_SnapReceive` | LB1 | `9` | `8` | 35 | END | 21 | 35 |
| ✅ EXACT | `Action_ReadDefender` | LB1 | `9` | `8` | 39 | START | 39 | 44 |
| ✅ EXACT | `Action_BlockSecondLevel` | WR3 | `5` | `4` | 45 | START | 45 | 81 |
| ✅ EXACT | `Action_Keep` | LB1 | `9` | `8` | 45 | START | 45 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB1 | `9` | `8` | 59 | START | 59 | 68 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 81 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 148 | 128 | inferred_complete_timeline |
| `Action_None` | 152 | 210 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 49 | 29 | inferred_complete_timeline |
| `Action_None` | 53 | 210 | 158 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 45 | 81 | 37 | inferred_complete_timeline |
| `Action_None` | 82 | 194 | 113 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 93 | 73 | inferred_complete_timeline |
| `Action_None` | 95 | 210 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 44 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 81 | 20 | inferred_complete_timeline |
| `Action_None` | 82 | 115 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 81 | 58 | inferred_complete_timeline |
| `Action_None` | 82 | 210 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 46 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 81 | 58 | inferred_complete_timeline |
| `Action_None` | 82 | 210 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 81 | 58 | inferred_complete_timeline |
| `Action_None` | 82 | 189 | 108 | inferred_complete_timeline |
| `Action_None` | 192 | 210 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 70 | 50 | inferred_complete_timeline |
| `Action_None` | 80 | 210 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–41
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 41 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 68 | 48 | inferred_complete_timeline |
| `Action_None` | 72 | 86 | 15 | inferred_complete_timeline |
| `Action_None` | 88 | 93 | 6 | inferred_complete_timeline |
| `Action_None` | 98 | 109 | 12 | inferred_complete_timeline |
| `Action_None` | 115 | 210 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_SnapReceive` | 21 | 35 | 15 | inferred_complete_timeline |
| `Action_None` | 36 | 38 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 39 | 44 | 6 | inferred_complete_timeline |
| `Action_Keep` | 45 | 58 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 59 | 68 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 76 | 77 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_BallSnap` | 21 | 35 | 15 | inferred_complete_timeline |
| `Action_None` | 36 | 210 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 117 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 57–210 | 144 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 93–103 | 11 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 107–210 | 104 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 133–136 | 4 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 137–210 | 67 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 141–165 | 4 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 143–165 | 9 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 153–210 | 58 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 163–210 | 48 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 173–174 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 49 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [21-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-194] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-117] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [59-68] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [76-77] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-93] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-70] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-68] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-86] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-93] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-109] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-49] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-148] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [24-44] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-115] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-41] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-189] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [24-46] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-92] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-103] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-174] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-149] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '31' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_377'; source metadata written as null.

</details>