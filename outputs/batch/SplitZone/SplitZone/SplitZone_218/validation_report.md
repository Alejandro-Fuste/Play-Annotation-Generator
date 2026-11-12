# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_218`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_218/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 106 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '15' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '0' (RG) duration 111 frames exceeds threshold 90 frames [start=94, end=204].
> - Segment 'Action_ZoneBlock' for track '4' has invalid range: start=94, end=90. Clamping end to start.
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (RT) duration 111 frames exceeds threshold 90 frames [start=94, end=204].
> - Action 'Action_ZoneBlock' range [94-116] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [160-161] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-212] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-220] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-141] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-307] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-328] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-356] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [122-131] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-107] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-184] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-198] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-173] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-109] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-284] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-338] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [103-123] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [125-138] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [141-184] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [91-167] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-93] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-110] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [117-166] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-288] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-359] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [105-144] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-215] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-179] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-219] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-135] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-111] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-204] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-20] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-102] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-126] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-177] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-165] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-190] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-209] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-157] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-199] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-359] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-187] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-211] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-246] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-337] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-353] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-199] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-208] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-216] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [179-192] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-203] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-359] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-359] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-224] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-241] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-328] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-331] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-237] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-282] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-275] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-359] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-345] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-303] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-359] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-321] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [335-337] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-344] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [349-351] for track '38' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.