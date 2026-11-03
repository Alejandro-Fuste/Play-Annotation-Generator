# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_41

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_41`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 269
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 123
- **Validation Warnings:** 146
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 1
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 109
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Kicker | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_AttemptRecovery` | Onside_Recovery_Front6 | defense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Onside_Recovery_Front6 | defense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `1` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `10` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `12` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `13` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `16` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `2` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `3` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `4` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `5` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `6` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `8` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `3` | `3` | 2 | START | 2 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Kicker | `3` | `3` | 65 | START | 65 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_AttemptRecovery` | Onside_Recovery_Front6 | `9` | `9` | 134 | START | 137 | 145 |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Onside_Recovery_Front6 | `9` | `9` | 181 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_KickApproach` | 2 | 64 | 63 | inferred_complete_timeline |
| `Action_KickBall` | 65 | 96 | 32 | inferred_complete_timeline |
| `Action_KickBall` | 100 | 162 | 63 | inferred_complete_timeline |
| `Action_KickBall` | 164 | 168 | 5 | inferred_complete_timeline |
| `Action_KickBall` | 172 | 175 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 39 | 38 | inferred_complete_timeline |
| `Action_None` | 41 | 269 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–41
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 41 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 151 | 150 | inferred_complete_timeline |
| `Action_None` | 155 | 162 | 8 | inferred_complete_timeline |
| `Action_None` | 172 | 173 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 216 | 215 | inferred_complete_timeline |
| `Action_None` | 219 | 221 | 3 | inferred_complete_timeline |
| `Action_None` | 223 | 229 | 7 | inferred_complete_timeline |
| `Action_None` | 231 | 233 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 152 | 151 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 159 | 168 | 10 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_None` | 178 | 180 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 157 | 156 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_None` | 195 | 228 | 34 | inferred_complete_timeline |
| `Action_None` | 230 | 232 | 3 | inferred_complete_timeline |
| `Action_None` | 250 | 258 | 9 | inferred_complete_timeline |
| `Action_None` | 260 | 269 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 38 | 37 | inferred_complete_timeline |
| `Action_None` | 40 | 45 | 6 | inferred_complete_timeline |
| `Action_None` | 47 | 115 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 38 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 116 | 115 | inferred_complete_timeline |
| `Action_None` | 121 | 129 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 118 | 117 | inferred_complete_timeline |
| `Action_None` | 120 | 132 | 13 | inferred_complete_timeline |
| `Action_None` | 137 | 139 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 82 | 81 | inferred_complete_timeline |
| `Action_None` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_None` | 93 | 163 | 71 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 186 | 230 | 45 | inferred_complete_timeline |
| `Action_None` | 233 | 238 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 168 | 167 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 123 | 122 | inferred_complete_timeline |
| `Action_None` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 147 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 93 | 92 | inferred_complete_timeline |
| `Action_None` | 97 | 130 | 34 | inferred_complete_timeline |
| `Action_None` | 137 | 138 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 129 | 128 | inferred_complete_timeline |
| `Action_None` | 157 | 158 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front6 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 127 | 9 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 137 | 145 | 9 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 147 | 151 | 5 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 167 | 173 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 45–206 | 158 | 5 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 59–116 | 56 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 86–93 | 6 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 102–103 | 2 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 105–191 | 76 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 111–269 | 147 | 6 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 113–215 | 103 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 138–140 | 3 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 149–173 | 22 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 160–223 | 58 | 5 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 169–184 | 16 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 179–269 | 84 | 4 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 185–208 | 24 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 201–216 | 10 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 211–226 | 8 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 213–216 | 4 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 218–219 | 2 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 220–269 | 48 | 3 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 231–257 | 15 | 2 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 244–269 | 26 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 254–269 | 5 | 2 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 259–260 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickBall` and target `3` (4 segments found)
- ⚠️ Ambiguous match for action `Action_AttemptRecovery` and target `9` (3 segments found)
- ❌ Missing segment for action `Action_SecureRecovery` on target `9` (Onside_Recovery_Front6)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Onside_Recovery_Front4` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Onside_Recovery_Front6` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Onside_Recovery_Front5` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 98 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_SecureRecovery' for track '9' has invalid range: start=181, end=173. Clamping end to start.
- ⚠️ Action 'Action_None' range [2-82] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-163] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-230] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-238] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-157] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-228] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-258] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-151] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-162] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [65-96] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [100-162] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [164-168] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [172-175] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-216] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-229] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-118] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-132] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-39] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-93] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-130] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-152] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-168] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-110] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-127] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [137-145] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [147-151] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [167-173] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-116] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-129] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-168] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-41] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-38] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-45] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-115] for track '13' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-123] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-147] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-129] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-38] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-145] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-172] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-198] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-94] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-113] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-117] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-191] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-122] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-233] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-247] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-256] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-215] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-163] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-173] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-198] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-209] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-219] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-184] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-207] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-232] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-208] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-216] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-216] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-251] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-241] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-257] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '39' has 1 frames without a visible bounding box.
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

</details>