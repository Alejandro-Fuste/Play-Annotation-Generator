# Play-Annotation-Generator Annotation Review — Post10to15_11

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_11`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `6` | `6` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | WR1 | offense | `8` | `8` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 12 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 10 | START | 10 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `18` | `18` | 13 | START | 25 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 13 | START | 13 | 36 |
| ✅ EXACT | `Action_PassBlock` | LT | `20` | `20` | 13 | START | 13 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `6` | `6` | 13 | START | 13 | 88 |
| ✅ EXACT | `Action_PassBlock` | RG | `9` | `9` | 13 | START | 13 | 150 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 24 | END | 10 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | WR1 | `8` | `8` | 25 | START | 25 | 118 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 68 | START | 68 | 77 |

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
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 10 | 24 | 15 | inferred_complete_timeline |
| `Action_None` | 25 | 62 | 38 | inferred_complete_timeline |
| `Action_None` | 65 | 67 | 3 | inferred_complete_timeline |
| `Action_ThrowPass` | 68 | 77 | 10 | inferred_complete_timeline |
| `Action_None` | 78 | 150 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 51 | 42 | inferred_complete_timeline |
| `Action_None` | 53 | 61 | 9 | inferred_complete_timeline |
| `Action_None` | 65 | 82 | 18 | inferred_complete_timeline |
| `Action_None` | 84 | 117 | 34 | inferred_complete_timeline |
| `Action_None` | 127 | 129 | 3 | inferred_complete_timeline |
| `Action_None` | 131 | 150 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_RunPostRoute` | 25 | 118 | 94 | inferred_complete_timeline |
| `Action_RunPostRoute` | 120 | 142 | 23 | inferred_complete_timeline |
| `Action_RunPostRoute` | 144 | 150 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 150 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 150 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 73 | 64 | inferred_complete_timeline |
| `Action_None` | 78 | 129 | 52 | inferred_complete_timeline |
| `Action_None` | 131 | 149 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 55 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 36 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 98 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 102 | 150 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 10 | 24 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 45 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 55 | 60 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 121 | 55 | inferred_complete_timeline |
| `Action_PassBlock` | 135 | 150 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 150 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 88 | 76 | inferred_complete_timeline |
| `Action_PassBlock` | 99 | 102 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 57 | 48 | inferred_complete_timeline |
| `Action_None` | 59 | 65 | 7 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_None` | 71 | 81 | 11 | inferred_complete_timeline |
| `Action_None` | 87 | 123 | 37 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 150 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–37
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 30 | 21 | inferred_complete_timeline |
| `Action_None` | 32 | 37 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 58 | 49 | inferred_complete_timeline |
| `Action_None` | 60 | 118 | 59 | inferred_complete_timeline |
| `Action_None` | 137 | 150 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 91 | 82 | inferred_complete_timeline |
| `Action_None` | 102 | 150 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 75 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–28
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 28 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 98 | 89 | inferred_complete_timeline |
| `Action_None` | 119 | 125 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 79 | 70 | inferred_complete_timeline |
| `Action_None` | 81 | 91 | 11 | inferred_complete_timeline |
| `Action_None` | 101 | 107 | 7 | inferred_complete_timeline |
| `Action_None` | 111 | 113 | 3 | inferred_complete_timeline |
| `Action_None` | 116 | 121 | 6 | inferred_complete_timeline |
| `Action_None` | 134 | 150 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 54 | 45 | inferred_complete_timeline |
| `Action_None` | 57 | 61 | 5 | inferred_complete_timeline |
| `Action_None` | 74 | 78 | 5 | inferred_complete_timeline |
| `Action_None` | 82 | 121 | 40 | inferred_complete_timeline |
| `Action_None` | 125 | 128 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 140 | 131 | inferred_complete_timeline |
| `Action_None` | 142 | 144 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 150 | 141 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 32–100 | 56 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 69–150 | 68 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 72–150 | 51 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 93–150 | 52 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 99–100 | 2 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 104–122 | 15 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 131–150 | 20 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 136–150 | 15 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 136–150 | 15 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 142–150 | 9 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 149–150 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunPostRoute` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 81 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [10–24], lower_priority='Action_PassBlock' annotated_start=13, effective_Action_PassBlock_start=25.
- ⚠️ Action 'Action_None' range [10-73] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-129] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-149] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-150] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-54] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-61] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-78] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-121] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-128] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-28] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-51] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-61] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-82] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-117] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-88] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [99-102] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-57] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-65] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-81] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-123] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-150] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [25-118] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [120-142] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [144-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-58] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-118] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-75] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-62] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-67] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' for track '12' starts at frame 68, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ThrowPass' range [68-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-150] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-98] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-125] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-140] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-79] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-91] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-45] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [55-60] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [64-65] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-121] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [135-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-36] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-98] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [102-150] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-55] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-30] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-37] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-69] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-78] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-92] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-75] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-111] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-122] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-150] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-150] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-150] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-150] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '32' has 1 frames without a visible bounding box.
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