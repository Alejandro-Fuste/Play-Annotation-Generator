# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_202`
- **Input XML**: `outputs/batch/Power/Power/Power_202/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 25 |
| Ball Tracks | 1 |
| CSV events parsed | 11 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [11-184] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-265] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-204] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-155] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-190] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [116-129] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [140-166] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-215] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-226] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-231] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-256] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-288] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [116-148] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-200] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-196] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-230] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-69] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-140] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-153] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-157] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-299] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-185] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-205] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-70] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [116-128] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-172] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-183] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-48] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-132] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-245] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [116-146] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-46] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-64] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-151] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-167] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-240] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-264] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-134] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-189] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-214] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-200] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-139] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-149] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-155] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-201] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-219] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-170] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-258] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-205] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-233] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-236] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-243] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-298] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-253] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-277] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-287] for track '25' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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