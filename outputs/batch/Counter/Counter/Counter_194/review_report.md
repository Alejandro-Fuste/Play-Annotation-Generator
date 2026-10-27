# Play-Annotation-Generator Annotation Review — Counter_194

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_194`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 19
- **Ball Tracks:** 0
- **Action Segments:** 42
- **Validation Warnings:** 37
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 26
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | WR1 | offense | `1` | `0` |
| ✅ EXACT | `Action_DownBlock` | WR1 | offense | `1` | `0` |
| ✅ EXACT | `Action_DownBlock` | DT2 | defense | `9` | `8` |
| ✅ EXACT | `Action_PullBlock` | CB2 | defense | `6` | `5` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ❌ MISSING SEGMENT | `Action_Handoff` | QB | offense | `4` | `3` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | DT1 | defense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 0 | START | 2 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `20` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `21` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `22` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 10 |
| ✅ EXACT | `Action_BallSnap` | WR1 | `1` | `0` | 11 | START | 11 | 15 |
| ✅ EXACT | `Action_DownBlock` | WR1 | `1` | `0` | 16 | START | 16 | 33 |
| ✅ EXACT | `Action_DownBlock` | DT2 | `9` | `8` | 16 | START | 16 | 54 |
| ✅ EXACT | `Action_PullBlock` | CB2 | `6` | `5` | 16 | START | 16 | 54 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `2` | `1` | 16 | START | 16 | 54 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 27 | END | 11 | 27 |
| ❌ MISSING SEGMENT | `Action_Handoff` | QB | `4` | `3` | 34 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | DT1 | `8` | `7` | 51 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 54 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–33
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 27 | 17 | inferred_complete_timeline |
| `Action_None` | 28 | 33 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–35
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 35 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–33
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 11 | 15 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 16 | 33 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 2–3
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 3 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–23
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 23 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 125–150
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 125 | 150 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 72–73
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 72 | 73 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 71–150
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 71 | 87 | 17 | inferred_complete_timeline |
| `Action_None` | 89 | 150 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 16 | 54 | 39 | inferred_complete_timeline |
| `Action_None` | 55 | 120 | 66 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 150 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–27
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 13 | 16 | 4 | inferred_complete_timeline |
| `Action_None` | 21 | 27 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 38 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–4
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 16 | 54 | 39 | inferred_complete_timeline |
| `Action_None` | 55 | 148 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `18`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 65–126
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 65 | 126 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–19
- **Visible Samples:** 13

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 10 | 1 | inferred_complete_timeline |
| `Action_None` | 11 | 11 | 1 | inferred_complete_timeline |
| `Action_None` | 18 | 19 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PullBlock` | 16 | 54 | 39 | inferred_complete_timeline |
| `Action_None` | 55 | 136 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `19`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 67–150
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 67 | 141 | 75 | inferred_complete_timeline |
| `Action_None` | 145 | 150 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–17
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 17 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `23` | Position_Unknown | Team_Unknown | 135–150 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_Handoff` on target `4` (QB)
- ❌ Missing segment for action `Action_BallCarry` on target `8` (DT1)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ 1 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 1 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 2 |
| Missing visible bounding boxes during action | 28 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '14' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '15' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_Handoff' for track '3' has invalid range: start=34, end=33. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '7' has invalid range: start=51, end=4. Clamping end to start.
- ⚠️ Action 'Action_DownBlock' range [16-33] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '2' starts at frame 11, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [11-11] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-19] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-33] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-17] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-136] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-23] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-148] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-16] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-27] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-38] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-35] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-3] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-126] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-141] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.

</details>