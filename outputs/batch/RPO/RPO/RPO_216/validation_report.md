# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_216`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_216/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [141-149] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-124] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-232] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-238] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-257] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-265] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-294] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-298] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-159] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-190] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-277] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-92] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-299] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' for track '6' starts at frame 141, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [141-154] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-115] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-255] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [261-271] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-285] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-299] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [84-140] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-170] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-101] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-299] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [84-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-178] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [186-299] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [83-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-85] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-169] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [84-131] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-85] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-164] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-210] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-172] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-101] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-298] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-153] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-164] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-155] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-157] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-299] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-164] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-169] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-227] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-216] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-299] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-221] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-238] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-267] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [263-266] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-280] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [276-299] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-296] for track '36' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.