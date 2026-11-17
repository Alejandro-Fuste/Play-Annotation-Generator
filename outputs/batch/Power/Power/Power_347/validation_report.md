# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_347`
- **Input XML**: `outputs/batch/Power/Power/Power_347/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [16-162] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-248] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-123] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-271] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-243] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-277] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-292] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-212] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-170] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-228] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-231] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-237] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-271] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-278] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-204] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-154] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-92] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [65-139] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-329] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-104] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-158] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-276] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-56] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-222] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [65-119] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-155] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-165] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-192] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-226] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-87] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-329] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-182] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-204] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-270] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-170] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-174] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-190] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-298] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-302] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-305] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-329] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-215] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-228] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-237] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-300] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-318] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-324] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-317] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-327] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-315] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-326] for track '34' has 2 frames without a visible bounding box.
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