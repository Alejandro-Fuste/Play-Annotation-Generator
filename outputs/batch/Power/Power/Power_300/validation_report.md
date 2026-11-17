# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_300`
- **Input XML**: `outputs/batch/Power/Power/Power_300/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 600: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [10-166] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-125] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-262] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [95-114] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [117-155] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-241] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-248] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-179] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-132] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-179] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-162] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [95-162] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-170] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-193] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-155] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-171] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-41] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-57] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-62] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-93] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-128] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-187] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-12] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-15] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-19] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-30] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-38] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-99] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-126] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-135] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-106] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-112] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-117] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-125] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-137] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-173] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-203] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-144] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-147] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-160] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-176] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-194] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-249] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-166] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-174] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-190] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-223] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-212] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-258] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-264] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-265] for track '25' has 2 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.