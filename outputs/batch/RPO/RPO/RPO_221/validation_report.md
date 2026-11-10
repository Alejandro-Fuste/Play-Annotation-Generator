# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_221`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_221/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 55 |
| Player Tracks | 55 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 171 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_None' range [59-181] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-304] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-316] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-303] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-221] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-249] for track '2' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [252-255] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-268] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-295] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-299] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-92] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-329] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-191] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-211] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [224-235] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-240] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-306] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [308-329] for track '5' has 5 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [67-320] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [323-329] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-228] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-252] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-197] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-208] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-216] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-194] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-216] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-142] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-177] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-197] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-131] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-151] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-66] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-69] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [72-82] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-203] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-307] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-297] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-126] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-138] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '20' starts at frame 60, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [60-60] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-74] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-96] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-62] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-78] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-132] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-214] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-313] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-73] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-87] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-92] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-111] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-97] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-101] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-108] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-113] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-144] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-329] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-169] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-206] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-176] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-178] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-182] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-207] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-259] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-329] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-204] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-245] for track '38' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [255-259] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-268] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-301] for track '38' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [303-318] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-323] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-215] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-225] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-231] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-316] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-324] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-240] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-245] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-274] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-302] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-314] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-262] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-291] for track '45' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [305-306] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-284] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-293] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [306-309] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-292] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-313] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-323] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-323] for track '54' has 1 frames without a visible bounding box.
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
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Player track '53' has undefined position. Will map to Position_Unknown.
> - Player track '53' has undefined team_side. Will map to Team_Unknown.
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.