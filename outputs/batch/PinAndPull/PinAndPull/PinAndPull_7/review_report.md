# Play-Annotation-Generator Annotation Review — PinAndPull_7

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PinAndPull_7`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_PinAndPull`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 122
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 13 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 14 | START | 14 | 15 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | C | `15` | `14` | 15 | END | N/A | N/A |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `10` | `9` | 17 | START | 17 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `7` | `6` | 17 | START | 17 | 28 |
| ✅ EXACT | `Action_PullBlock` | RG | `8` | `7` | 17 | START | 17 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | `16` | `15` | 17 | START | 28 | 32 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `10` | 31 | START | 31 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `3` | 51 | START | 51 | 87 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 111 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_Handoff` | 31 | 50 | 20 | inferred_complete_timeline |
| `Action_None` | 51 | 84 | 34 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–319
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_BallCarry` | 51 | 87 | 37 | inferred_complete_timeline |
| `Action_BallCarry` | 94 | 319 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 39 | 26 | inferred_complete_timeline |
| `Action_None` | 43 | 52 | 10 | inferred_complete_timeline |
| `Action_None` | 58 | 185 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 113 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 58 | 45 | inferred_complete_timeline |
| `Action_None` | 60 | 64 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–21
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_BallSnap` | 14 | 15 | 2 | inferred_complete_timeline |
| `Action_None` | 16 | 21 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PullBlock` | 17 | 111 | 95 | inferred_complete_timeline |
| `Action_None` | 112 | 389 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 17 | 28 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 32 | 111 | 80 | inferred_complete_timeline |
| `Action_None` | 112 | 161 | 50 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 19 | 6 | inferred_complete_timeline |
| `Action_None` | 28 | 39 | 12 | inferred_complete_timeline |
| `Action_None` | 42 | 44 | 3 | inferred_complete_timeline |
| `Action_None` | 57 | 88 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–30
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 23 | 10 | inferred_complete_timeline |
| `Action_None` | 26 | 30 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–19
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 19 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 119 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 389 | 376 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 27 | 14 | inferred_complete_timeline |
| `Action_None` | 29 | 109 | 81 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–42 | 43 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 28–94 | 58 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 33–108 | 55 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 36–118 | 83 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 44–126 | 83 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 63–216 | 154 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 68–69 | 2 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 69–101 | 33 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 84–89 | 6 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 88–208 | 105 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 102–203 | 67 | 5 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 103–217 | 112 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 167–319 | 153 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 186–389 | 204 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 208–214 | 7 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 209–389 | 177 | 3 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 218–319 | 102 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 227–319 | 93 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 251–312 | 32 | 4 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 258–389 | 89 | 2 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 320–389 | 70 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 320–389 | 70 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 320–389 | 70 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 320–389 | 70 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 320–389 | 70 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 320–389 | 70 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 320–389 | 70 | 1 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 320–389 | 70 | 1 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 320–389 | 70 | 1 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 327–389 | 63 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_SnapReceive` on target `15` (C)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '6' (RT) duration 95 frames exceeds threshold 90 frames [start=17, end=111].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '7' (RG) duration 95 frames exceeds threshold 90 frames [start=17, end=111].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [14–15], lower_priority='Action_SnapReceive' annotated_start=14, effective_Action_SnapReceive_start=16.
- ⚠️ Action 'Action_None' range [14-119] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-113] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-39] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-52] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-185] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [51-87] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [94-319] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-389] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-27] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-109] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [17-28] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [32-111] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-161] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-58] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-64] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [17-42] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-84] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-19] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-39] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-44] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-88] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-19] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-23] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-30] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-21] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [28-32] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [42-94] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-34] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-65] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-108] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-118] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-126] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-216] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-101] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-89] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-190] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-114] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-156] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-191] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-114] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-217] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-319] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-214] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-319] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-319] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-295] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-312] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-275] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.

</details>