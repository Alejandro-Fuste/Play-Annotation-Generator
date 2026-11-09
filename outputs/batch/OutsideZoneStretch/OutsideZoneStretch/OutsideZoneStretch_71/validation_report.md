# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_71`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_71/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [0-359] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-336] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-221] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-359] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-236] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-241] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-287] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-359] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-182] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-343] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-359] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-322] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-333] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-223] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-226] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-104] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [106-107] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [127-128] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-198] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-157] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-165] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-191] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-347] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-135] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-163] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-170] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-177] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-181] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-190] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-197] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-202] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-214] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-239] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-236] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-270] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-328] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-331] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-340] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-356] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [333-335] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-352] for track '30' has 1 frames without a visible bounding box.
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