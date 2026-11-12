# Play-Annotation-Generator Annotation Review — SplitZone_115

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_115`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 75
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
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `6` | `6` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 11 | START | 12 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 11 | START | 12 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 11 | START | 12 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 11 | START | 12 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 11 | START | 12 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 11 | START | 12 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `23` | `Group` | 11 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 11 | START | 12 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 11 | START | 12 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 11 | START | 12 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `8` | `Group` | 11 | START | 12 | 21 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 15 | START | 15 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `14` | `14` | 18 | START | 18 | 38 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `18` | `18` | 18 | START | 18 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `19` | 18 | START | 18 | 29 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `20` | `20` | 18 | START | 29 | 113 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `6` | `6` | 18 | START | 18 | 113 |
| ✅ EXACT | `Action_SplitBlock` | HB | `8` | `8` | 22 | START | 22 | 113 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `5` | 28 | END | 15 | 28 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `5` | 29 | START | 29 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `4` | 43 | START | 43 | 76 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 113 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 12–135
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 14 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 15 | 28 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 29 | 42 | 14 | inferred_complete_timeline |
| `Action_None` | 43 | 135 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 12–210
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 42 | 31 | inferred_complete_timeline |
| `Action_BallCarry` | 43 | 76 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 83 | 181 | 99 | inferred_complete_timeline |
| `Action_BallCarry` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 197 | 200 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 202 | 205 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 12–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 21 | 10 | inferred_complete_timeline |
| `Action_SplitBlock` | 22 | 113 | 92 | inferred_complete_timeline |
| `Action_None` | 114 | 210 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 12–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 14 | 3 | inferred_complete_timeline |
| `Action_None` | 15 | 210 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 12–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 14 | 3 | inferred_complete_timeline |
| `Action_None` | 15 | 128 | 114 | inferred_complete_timeline |
| `Action_None` | 131 | 210 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `23`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 39–210
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 39 | 210 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 12–160
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 17 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 113 | 96 | inferred_complete_timeline |
| `Action_None` | 114 | 160 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 12–59
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 17 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 38 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 59 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 12–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 14 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 15 | 28 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 113 | 85 | inferred_complete_timeline |
| `Action_None` | 114 | 150 | 37 | inferred_complete_timeline |
| `Action_None` | 152 | 210 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 12–210
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 17 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 29 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 113 | 80 | inferred_complete_timeline |
| `Action_None` | 114 | 210 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 12–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 17 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 113 | 96 | inferred_complete_timeline |
| `Action_None` | 114 | 210 | 97 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 12–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 14 | 3 | inferred_complete_timeline |
| `Action_None` | 15 | 48 | 34 | inferred_complete_timeline |
| `Action_None` | 51 | 210 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 12–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 14 | 3 | inferred_complete_timeline |
| `Action_None` | 15 | 210 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 12–59
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 14 | 3 | inferred_complete_timeline |
| `Action_None` | 15 | 59 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 12–84
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 14 | 3 | inferred_complete_timeline |
| `Action_None` | 15 | 78 | 64 | inferred_complete_timeline |
| `Action_None` | 82 | 84 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 12–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 14 | 3 | inferred_complete_timeline |
| `Action_None` | 15 | 210 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 12–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 14 | 3 | inferred_complete_timeline |
| `Action_None` | 15 | 210 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 12–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 14 | 3 | inferred_complete_timeline |
| `Action_None` | 15 | 210 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 12–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 14 | 3 | inferred_complete_timeline |
| `Action_None` | 15 | 210 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 12–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 14 | 3 | inferred_complete_timeline |
| `Action_None` | 15 | 210 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 12–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 14 | 3 | inferred_complete_timeline |
| `Action_None` | 15 | 210 | 196 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 12–43 | 32 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 12–210 | 199 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 12–32 | 21 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 67–210 | 136 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 98–123 | 16 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 117–120 | 4 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 118–210 | 93 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 120–210 | 91 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 144–164 | 10 | 3 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 159–210 | 52 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `20` (C): Annotated start 18 != Inferred start 29
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (RT) duration 96 frames exceeds threshold 90 frames [start=18, end=113].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (LT) duration 96 frames exceeds threshold 90 frames [start=18, end=113].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (RG) duration 96 frames exceeds threshold 90 frames [start=18, end=113].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (C) duration 96 frames exceeds threshold 90 frames [start=18, end=113].
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [15–28], lower_priority='Action_ZoneBlock' annotated_start=18, effective_Action_ZoneBlock_start=29.
- ⚠️ Action 'Action_None' range [15-128] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-48] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-210] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [43-76] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [83-181] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [193-194] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [197-200] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [202-205] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [209-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-135] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-210] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-43] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-78] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-84] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-59] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-210] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-210] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-38] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-59] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-113] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-160] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-29] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-150] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-32] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-119] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-107] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-164] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
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

</details>