# Play-Annotation-Generator Annotation Review — WRSlowScreens_30

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `WRSlowScreens_30`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_WRSlowScreens`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 41
- **Ball Tracks:** 2
- **Action Segments:** 97
- **Validation Warnings:** 123
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `3` | `3` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_ReleaseToScreen` | DE1 | defense | `11` | `11` |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_RunAfterCatch` | Position_Unknown | Team_Unknown | `44` | `31` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `8` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `9` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 2 | START | 2 | 7 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `10` | `10` | 5 | START | 8 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `16` | `16` | 5 | START | 5 | 22 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 5 | START | 5 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `2` | `2` | 5 | START | 5 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `3` | `3` | 5 | START | 5 | 139 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `17` | `17` | 7 | END | 2 | 5 |
| ✅ EXACT | `Action_ReleaseToScreen` | DE1 | `11` | `11` | 56 | START | 56 | 81 |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | `17` | `17` | 73 | START | 73 | 84 |
| ✅ EXACT | `Action_RunAfterCatch` | Position_Unknown | `44` | `31` | 121 | START | 121 | 208 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 2 | 5 | 4 | inferred_complete_timeline |
| `Action_None` | 11 | 72 | 62 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 73 | 84 | 12 | inferred_complete_timeline |
| `Action_None` | 85 | 131 | 47 | inferred_complete_timeline |
| `Action_None` | 134 | 135 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 42 | 41 | inferred_complete_timeline |
| `Action_None` | 45 | 51 | 7 | inferred_complete_timeline |
| `Action_None` | 56 | 58 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–37
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 20 | 19 | inferred_complete_timeline |
| `Action_None` | 22 | 37 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 31 | 30 | inferred_complete_timeline |
| `Action_None` | 35 | 103 | 69 | inferred_complete_timeline |
| `Action_None` | 147 | 210 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 90 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 22 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 210 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 38 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 210 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 2 | 7 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 27 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 40 | 48 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 64 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 78 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 83 | 100 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 210 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 88 | 84 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 210 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 139 | 135 | inferred_complete_timeline |
| `Action_PassBlock` | 142 | 151 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 154 | 210 | 57 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 55 | 21 | inferred_complete_timeline |
| `Action_ReleaseToScreen` | 56 | 81 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 84 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 51 | 50 | inferred_complete_timeline |
| `Action_None` | 55 | 57 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 101 | 100 | inferred_complete_timeline |
| `Action_None` | 109 | 210 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 54 | 53 | inferred_complete_timeline |
| `Action_None` | 77 | 154 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 140 | 139 | inferred_complete_timeline |
| `Action_None` | 147 | 210 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 106 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 27 | 26 | inferred_complete_timeline |
| `Action_None` | 56 | 94 | 39 | inferred_complete_timeline |
| `Action_None` | 96 | 109 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 101 | 100 | inferred_complete_timeline |
| `Action_None` | 103 | 210 | 108 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `23` | Position_Unknown | Team_Unknown | 34–77 | 39 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 38–42 | 5 | 1 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 59–210 | 144 | 2 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 61–104 | 44 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 61–88 | 28 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 66–73 | 8 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 67–210 | 141 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 78–111 | 34 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 98–109 | 11 | 2 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 102–210 | 109 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 121–208 | 88 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 124–210 | 87 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 127–210 | 56 | 3 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 145–210 | 66 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 149–210 | 62 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 156–203 | 48 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 159–161 | 3 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 161–210 | 48 | 2 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 171–179 | 7 | 2 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 199–210 | 12 | 1 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `22` | `30` | 59 | 61 | 3 | 100.0% | None |
| `27` | `37` | 75 | 75 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [2–7], lower_priority='Action_PassBlock' annotated_start=5, effective_Action_PassBlock_start=8.
- ⚠️ Action 'Action_None' range [2-106] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-140] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-88] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-139] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [142-151] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [154-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-54] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-154] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-51] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-57] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-42] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-51] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-58] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-101] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-20] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-37] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-90] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [8-27] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [40-48] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [51-64] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-78] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [83-100] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReleaseToScreen' range [56-81] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-101] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-27] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-109] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-84] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-31] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-103] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-22] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [2-5] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-131] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-38] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-210] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-42] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-48] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-77] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-42] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-64] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-104] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-88] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-73] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-180] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-111] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-106] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-210] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [121-208] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-170] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-203] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-178] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_WRSlowScreens'.

</details>