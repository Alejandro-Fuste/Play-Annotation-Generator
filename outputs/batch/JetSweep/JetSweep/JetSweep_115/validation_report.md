# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_115`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_115/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [62–72], lower_priority='Action_ZoneBlock' annotated_start=64, effective_Action_ZoneBlock_start=73.
> - Action 'Action_PreSnap' range [0-89] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [91-257] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-116] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-269] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [123-153] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-148] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-140] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-158] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-269] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-126] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-114] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-81] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-136] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-159] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-184] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-16] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-75] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-85] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-155] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-154] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [121-161] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [173-174] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-189] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-269] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-232] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '26' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.