# Play-Annotation-Generator Annotation Review — BootPass_56

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_56`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 67
- **Validation Warnings:** 73
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ START CHANGED | `Action_RunBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `26` | `23` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `24` | `22` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | DE2 | defense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `9` | `Group` | 0 | START | 0 | 32 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 33 | START | 33 | 49 |
| ⚠️ START CHANGED | `Action_RunBlock` | C | `14` | `14` | 41 | START | 50 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `15` | `15` | 41 | START | 41 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `7` | `7` | 41 | START | 41 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `8` | `8` | 41 | START | 41 | 96 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 49 | END | 33 | 49 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `12` | `12` | 55 | START | 55 | 78 |
| ✅ EXACT | `Action_BootAway` | QB | `12` | `12` | 79 | START | 79 | 107 |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | `26` | `23` | 93 | START | 93 | 107 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `24` | `22` | 111 | START | 111 | 118 |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | DE2 | `0` | `0` | 234 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_SnapReceive` | 33 | 49 | 17 | inferred_complete_timeline |
| `Action_None` | 50 | 54 | 5 | inferred_complete_timeline |
| `Action_FakeHandoff` | 55 | 78 | 24 | inferred_complete_timeline |
| `Action_BootAway` | 79 | 107 | 29 | inferred_complete_timeline |
| `Action_None` | 108 | 139 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 169 | 137 | inferred_complete_timeline |
| `Action_None` | 172 | 210 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 95 | 63 | inferred_complete_timeline |
| `Action_None` | 99 | 116 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 67 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_RunBlock` | 41 | 53 | 13 | inferred_complete_timeline |
| `Action_RunBlock` | 113 | 141 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_RunBlock` | 41 | 84 | 44 | inferred_complete_timeline |
| `Action_RunBlock` | 97 | 112 | 16 | inferred_complete_timeline |
| `Action_RunBlock` | 114 | 118 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_BallSnap` | 33 | 49 | 17 | inferred_complete_timeline |
| `Action_RunBlock` | 50 | 120 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_RunBlock` | 41 | 96 | 56 | inferred_complete_timeline |
| `Action_RunBlock` | 98 | 100 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 109 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 93 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 102 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 210 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 109 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 210 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 210 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 210 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 151 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 210 | 178 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–98 | 99 | 2 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–126 | 127 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 42–78 | 37 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 53–210 | 154 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 56–65 | 10 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 72–73 | 2 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 80–210 | 131 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 84–209 | 126 | 3 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 137–210 | 73 | 2 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 143–210 | 68 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 145–210 | 66 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 153–210 | 58 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 194–210 | 17 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 202–210 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_RunBlock` for actor_track_id `14` (C): Annotated start 41 != Inferred start 50
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `8` (2 segments found)
- ❌ Missing segment for action `Action_SecureCatch` on target `0` (DE2)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 92: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_SecureCatch' for track '0' has invalid range: start=234, end=210. Clamping end to start.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [33–49], lower_priority='Action_RunBlock' annotated_start=41, effective_Action_RunBlock_start=50.
- ⚠️ Action 'Action_PreSnap' range [0-86] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-93] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-102] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-98] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-151] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-67] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-126] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-95] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-116] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [41-84] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [97-112] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [114-118] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [41-96] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [98-100] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-169] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-139] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-109] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [50-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [41-53] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [113-141] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-109] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-78] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-55] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-65] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-209] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-154] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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

</details>