# Play-Annotation-Generator Annotation Review — Counter_210

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_210`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 105
- **Validation Warnings:** 126
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 1
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | DT1 | defense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `12` | `11` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 58 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `13` | `12` | 59 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `13` | `12` | 60 | START | 63 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `2` | `1` | 60 | START | 60 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `4` | `3` | 60 | START | 60 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | DT1 | `8` | `7` | 60 | START | 60 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | `12` | `11` | 60 | START | 60 | 95 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 72 | END | 59 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `9` | `8` | 91 | START | 91 | 146 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 148 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–329
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_SnapReceive` | 59 | 72 | 14 | inferred_complete_timeline |
| `Action_None` | 73 | 90 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 91 | 146 | 56 | inferred_complete_timeline |
| `Action_BallCarry` | 159 | 228 | 70 | inferred_complete_timeline |
| `Action_BallCarry` | 230 | 232 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 236 | 270 | 35 | inferred_complete_timeline |
| `Action_BallCarry` | 278 | 329 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 75 | 17 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 147 | 9 | inferred_complete_timeline |
| `Action_None` | 151 | 177 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 76 | 18 | inferred_complete_timeline |
| `Action_None` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 122 | 135 | 14 | inferred_complete_timeline |
| `Action_None` | 149 | 151 | 3 | inferred_complete_timeline |
| `Action_None` | 174 | 184 | 11 | inferred_complete_timeline |
| `Action_None` | 187 | 192 | 6 | inferred_complete_timeline |
| `Action_None` | 200 | 329 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_DownBlock` | 60 | 85 | 26 | inferred_complete_timeline |
| `Action_DownBlock` | 87 | 148 | 62 | inferred_complete_timeline |
| `Action_None` | 149 | 318 | 170 | inferred_complete_timeline |
| `Action_None` | 325 | 328 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_DownBlock` | 60 | 111 | 52 | inferred_complete_timeline |
| `Action_DownBlock` | 138 | 144 | 7 | inferred_complete_timeline |
| `Action_None` | 212 | 222 | 11 | inferred_complete_timeline |
| `Action_None` | 225 | 329 | 105 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 58 | 7 | inferred_complete_timeline |
| `Action_None` | 59 | 146 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 100 | 42 | inferred_complete_timeline |
| `Action_None` | 110 | 115 | 6 | inferred_complete_timeline |
| `Action_None` | 120 | 266 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PullBlock` | 60 | 87 | 28 | inferred_complete_timeline |
| `Action_PullBlock` | 93 | 127 | 35 | inferred_complete_timeline |
| `Action_PullBlock` | 130 | 148 | 19 | inferred_complete_timeline |
| `Action_None` | 149 | 149 | 1 | inferred_complete_timeline |
| `Action_None` | 153 | 167 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–62
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 62 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 72 | 14 | inferred_complete_timeline |
| `Action_None` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_None` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_None` | 94 | 97 | 4 | inferred_complete_timeline |
| `Action_None` | 99 | 128 | 30 | inferred_complete_timeline |
| `Action_None` | 131 | 133 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 122 | 64 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 28–329 | 260 | 7 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 63–272 | 128 | 8 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 81–198 | 118 | 1 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 106–209 | 79 | 2 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 113–163 | 51 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 118–329 | 152 | 7 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 125–127 | 3 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 147–184 | 28 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 159–329 | 171 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 162–167 | 6 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 183–204 | 22 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 197–329 | 133 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 197–208 | 10 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 219–258 | 40 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 255–329 | 63 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 260–262 | 3 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 268–329 | 61 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 274–329 | 56 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 281–286 | 6 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 284–329 | 46 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 289–329 | 41 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 297–329 | 33 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 300–329 | 30 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `13` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (5 segments found)

### Track Identity Issues

- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 79 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_None' range [59-100] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-115] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-266] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [60-111] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [138-144] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-222] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-75] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-147] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-177] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [60-85] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [87-148] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-318] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-328] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-122] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-76] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-184] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-192] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-72] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-78] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-128] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [60-87] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [93-127] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [130-148] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '7' starts at frame 149, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [149-149] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-167] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [91-146] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [159-228] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [230-232] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [236-270] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-62] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-146] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [60-95] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [112-119] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-185] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [63-73] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [76-80] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [82-89] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [95-96] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [108-126] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-198] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-151] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-209] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-163] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-157] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-206] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-221] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-230] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-239] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-157] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-184] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-167] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-204] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-208] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-258] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-257] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-312] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-286] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-329] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>