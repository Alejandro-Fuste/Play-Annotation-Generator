# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_2`
- **Input XML**: `outputs/batch/Power/Power/Power_2/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 6: Duplicate assignment for track ID '22' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Segment 'Action_DownBlock' for track '7' has invalid range: start=106, end=9. Clamping end to start.
> - Action 'Action_PreSnap' range [0-9] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-269] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-11] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-106] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-11] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-11] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-161] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-154] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-161] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-178] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-135] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-183] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-124] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-151] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-22] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-226] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [106-113] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [116-128] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [135-146] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-189] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-105] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-26] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-131] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-136] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-162] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-215] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-47] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-230] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-269] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-144] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-159] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-170] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-198] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-182] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-188] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-221] for track '36' has 2 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.