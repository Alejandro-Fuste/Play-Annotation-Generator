# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_140`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_140/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '8' has invalid range: start=121, end=117. Clamping end to start.
> - Action 'Action_None' range [118-275] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [283-294] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-259] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-280] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-276] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-169] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-280] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-297] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [137-299] for track '8' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [118-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-261] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-280] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-287] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-286] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-181] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-208] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-231] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-243] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-163] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-179] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-142] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-268] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-284] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-298] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-146] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [153-154] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-149] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-168] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-299] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-194] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-214] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-260] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-299] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-247] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-268] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '28' has 1 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_140'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.