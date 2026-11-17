# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_307`
- **Input XML**: `outputs/batch/Power/Power/Power_307/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [7-215] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-248] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-299] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-134] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-234] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-119] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-155] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-187] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-211] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-219] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-246] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-299] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-175] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-299] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [79-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-209] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-212] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-273] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [79-140] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [79-167] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-189] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-299] for track '17' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [168-253] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-195] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-222] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-232] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-237] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-243] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-286] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-294] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-130] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-195] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-123] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-182] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-185] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-203] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-257] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-275] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-299] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-211] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-215] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-241] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-266] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-278] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-259] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-228] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-249] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-289] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-277] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-284] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-293] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-282] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-291] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-298] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-299] for track '34' has 1 frames without a visible bounding box.
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