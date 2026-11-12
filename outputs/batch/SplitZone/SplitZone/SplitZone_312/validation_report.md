# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_312`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_312/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_None' range [138-329] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-329] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-208] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-230] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-238] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-255] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-329] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-204] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-213] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-170] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-181] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [185-329] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-227] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [229-272] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [138-227] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-274] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-287] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-164] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-200] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-151] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-169] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-222] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [205-209] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-241] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-209] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-303] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-234] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-270] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-276] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-326] for track '31' has 4 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.