# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_87`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_87/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [42–54], lower_priority='Action_ZoneBlock' annotated_start=45, effective_Action_ZoneBlock_start=55.
> - Action 'Action_None' range [42-389] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-261] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-210] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-153] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-229] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [42-87] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-130] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_Handoff' range [72-83] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-237] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-200] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-204] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-213] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-227] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [232-389] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-267] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [42-222] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-389] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [84-117] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [127-296] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-97] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-114] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-139] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-152] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-109] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-137] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-165] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-198] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [212-217] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [45-70] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-212] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-118] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-153] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [161-190] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-223] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [45-64] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-194] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-211] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-225] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-223] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-230] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [42-53] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [70-73] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [77-96] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [100-115] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-389] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-41] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-54] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-108] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-112] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-215] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-165] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-204] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-228] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.