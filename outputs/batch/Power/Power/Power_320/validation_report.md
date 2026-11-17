# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_320`
- **Input XML**: `outputs/batch/Power/Power/Power_320/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 33 |
| Ball Tracks | 1 |
| CSV events parsed | 10 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 640: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [10-71] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-178] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-182] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-61] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-145] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-154] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-159] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [42-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-194] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-157] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-205] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-176] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [42-55] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [57-65] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [67-72] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-188] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-73] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-69] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-58] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-68] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-100] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-195] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-108] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-132] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-53] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-202] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-89] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-98] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-106] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-140] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-209] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-100] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-108] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-128] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-91] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-112] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-293] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-318] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-334] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-79] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-162] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-166] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-208] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-205] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-163] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-181] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-235] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-241] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-136] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-148] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-132] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-143] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-349] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-353] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-231] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-310] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-359] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-190] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-194] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-211] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-206] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-305] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-355] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-359] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-352] for track '33' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.