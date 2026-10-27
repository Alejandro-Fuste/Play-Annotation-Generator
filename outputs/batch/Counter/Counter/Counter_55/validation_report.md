# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_55`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_55/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 112 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_None' range [116-168] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-202] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-189] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-329] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [117-158] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [165-168] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-128] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-158] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-181] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [117-127] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [164-171] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [178-179] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [184-185] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [117-126] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [165-168] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [170-171] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [184-189] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-201] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-304] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [306-311] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-132] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-153] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-158] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-171] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-187] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-194] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-204] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-128] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-171] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-181] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-140] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-168] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-132] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-129] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-171] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-181] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-187] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-329] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [117-127] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [151-153] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [164-171] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [178-182] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [184-185] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-329] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [116-124] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-158] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [163-170] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-235] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-329] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-300] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-317] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.